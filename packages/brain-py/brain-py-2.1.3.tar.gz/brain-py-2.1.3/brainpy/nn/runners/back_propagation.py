# -*- coding: utf-8 -*-

import time
from typing import Union, Dict, Callable, Sequence

import jax.numpy as jnp
import numpy as np
from jax.tree_util import tree_map

import brainpy.losses as losses
import brainpy.math as bm
import brainpy.optimizers as optim
from brainpy.errors import UnsupportedError
from brainpy.nn.base import Node, Network
from brainpy.nn.utils import check_rnn_data_batch_size, serialize_kwargs
from brainpy.running.runner import Runner
from brainpy.tools.checking import check_dict_data, check_float
from brainpy.types import Tensor
from .rnn_trainer import RNNTrainer

__all__ = [
  'BPTT',
]

MANY2ONE = 'many2one'
MANY2MANY = 'many2many'


class BackPropagation(Runner):
  pass


class BPTT(RNNTrainer):
  """
  The trainer implementing back propagation through time (BPTT)
  for recurrent neural networks.

  """

  def __init__(
      self,
      target: Node,

      # arguments for BPTT trainer
      loss: Union[str, Callable],  # loss function
      optimizer: optim.Optimizer = None,  # optimizer
      max_grad_norm=None,
      shuffle_data=True,
      metrics=('loss',),
      jit=True,

      # common arguments for RNNTrainer
      **kwargs
  ):
    super(BPTT, self).__init__(target=target, **kwargs)

    # jit settings
    if isinstance(jit, bool):
      self.jit = {'fit': jit, 'predict': jit, 'loss': jit}
    elif isinstance(jit, dict):
      jit = {key: val for key, val in jit.items()}
      self.jit = {'fit': jit.pop('fit', True),
                  'predict': jit.pop('predict', True),
                  'loss': jit.pop('loss', True)}
      if len(jit):
        raise ValueError(f'Unknown jit setting for {jit.keys()}')
    else:
      raise ValueError(f'Unknown "jit" setting: {jit}')

    # optimizer
    if optimizer is None:
      lr = optim.ExponentialDecay(lr=0.025, decay_steps=1, decay_rate=0.99975)
      optimizer = optim.Adam(lr=lr)
    self.optimizer = optimizer

    # loss
    if isinstance(loss, str):
      loss = getattr(losses, loss)
    elif callable(loss):
      loss = loss
    else:
      raise UnsupportedError(f'Do not support {type(loss)} to specify the loss function. '
                             f'We only support str and callable function.')
    self.loss_fun = loss
    self._train_losses = None
    self._test_losses = None

    # target/output mapping types
    self._mapping_type = None

    # functions
    self._f_loss = dict()
    self._f_train = dict()
    self._f_grad = dict()

    # training parameters
    self.max_grad_norm = max_grad_norm  # gradient clipping
    self.shuffle_data = shuffle_data
    self.metrics = metrics

    # initialize the optimizer
    if not self.target.is_initialized:
      raise ValueError('Please initialize the target model first by calling "initialize()" function.')
    self.optimizer.register_vars(self.target.vars().subset(bm.TrainVar).unique())

  def predict(
      self,
      xs: Union[Tensor, Dict[str, Tensor]],
      forced_states: Dict[str, Tensor] = None,
      forced_feedbacks: Dict[str, Tensor] = None,
      reset=True,
      shared_kwargs: Dict = None,
      **kwargs
  ):
    """Predict a series of input data with the given target model.

    This function use the JIT compilation to accelerate the model simulation.
    Moreover, it can automatically monitor the node variables, states, inputs,
    feedbacks and its output, if users want.

    Parameters
    ----------
    xs: Tensor, dict
      The feedforward input data. It must be a 3-dimensional data
      which has the shape of `(num_sample, num_time, num_feature)`.
    forced_states: dict
      The fixed node states. Similar with ``xs``, each tensor in
      ``forced_states`` must be a tensor with the shape of
      `(num_sample, num_time, num_feature)`. Default None.
    forced_feedbacks: dict
      The fixed feedback states. Similar with ``xs``, each tensor in
      ``forced_states`` must be a tensor with the shape of
      `(num_sample, num_time, num_feature)`. Default None.
    shared_kwargs: dict
      Shared keyword arguments for the given target model.
    reset: bool
      Whether reset the model states. Default True.

    Returns
    -------
    output: Tensor, dict
      The model output.
    """
    # check forced states/feedbacks
    assert forced_states is None, (f'Currently {self.__class__.__name__} does '
                                   f'not support "forced_states"')
    assert forced_feedbacks is None, (f'Currently {self.__class__.__name__} does '
                                      f'not support "forced_feedbacks"')
    return super(BPTT, self).predict(xs=xs,
                                     forced_states=forced_states,
                                     forced_feedbacks=forced_feedbacks,
                                     reset=reset)

  def fit(
      self,
      train_data: Union[Callable, Sequence],
      test_data: Union[Callable, Sequence] = None,
      num_batch: int = 32,
      num_train: int = 100,
      num_report: int = 100,
      reset: bool = True,
      shared_kwargs: Dict = None,
      # current unsupported features
      forced_states: Dict[str, Tensor] = None,
      forced_feedbacks: Dict[str, Tensor] = None,
  ):
    """
    Fit the target model according to the given training and testing data.

    Parameters
    ----------
    train_data: callable, sequence of data
      It can be a callable function, or a tuple/list representing `(X, Y)` data.
      - Callable. This function should return a pair of `(X, Y)` data
      - Sequence. It should be a pair of `(X, Y)` train set.
        - ``X``: should be a tensor or a dict of tensors with the shape of
          `(num_sample, num_time, num_feature)`, where `num_sample` is
          the number of samples, `num_time` is the number of the time step,
          and `num_feature` is the number of features.
        - ``Y``: Target values. A tensor or a dict of tensors.
          - If the shape of each tensor is `(num_sample, num_feature)`,
            then we will only fit the model with the only last output.
          - If the shape of each tensor is `(num_sample, num_time, num_feature)`,
            then the fitting happens on the whole data series.
    test_data: callable, sequence of data
      Same as the ``train_data``. It can be a callable function,
      or a tuple/list representing `(X, Y)` data.
    num_batch: int
      The batch size. Default 32. This setting is used when users provide
      the ``train_data`` and ``test_data`` as a pair of `(X, Y)` data, rather
      than a function.
    num_train: int
      The number of training epoch. Default 100.
    num_report: int
      The number of step to report the progress. Default 100 training steps.
    reset: bool
      Whether reset the initial states of the target model.
    forced_states: optional, dict
      The forced node states.
    forced_feedbacks: optional, dict
      The forced node feedbacks.
    shared_kwargs: dict
      The shared keyword arguments for the target models.
    """
    # check forced states/feedbacks
    assert forced_states is None, (f'Currently {self.__class__.__name__} does '
                                   f'not support "forced_states"')
    assert forced_feedbacks is None, (f'Currently {self.__class__.__name__} does '
                                      f'not support "forced_feedbacks"')

    # training the model
    all_train_losses = []
    all_test_losses = []
    train_i = 0
    t0 = time.time()
    for _ in range(num_train):
      train_data_ = self._get_train_data(train_data, num_batch)

      # training set
      for x, y in train_data_:
        self._check_mapping_type(y)
        batch_size = check_rnn_data_batch_size(x)
        if reset:
          self.target.initialize(batch_size)
        loss = self.f_train(shared_kwargs)(x, y)
        all_train_losses.append(loss)
        train_i += 1
        if train_i % num_report == 0:
          t1 = time.time()
          print(f'Train {train_i} steps, use {t1 - t0:.4f} s, train loss {round(float(loss), 5)}')
          t0 = t1

      # testing set
      test_data_ = self._get_test_data(test_data, num_batch)
      if test_data_ is not None:
        for x, y in test_data_:
          self._check_mapping_type(y)
          batch_size = check_rnn_data_batch_size(x)
          if reset:
            self.target.initialize(batch_size)
          loss = self.f_loss(shared_kwargs)(x, y)
          all_test_losses.append(loss)

    self._train_losses = bm.asarray(all_train_losses)
    self._test_losses = bm.asarray(all_test_losses)

  def f_grad(self, shared_kwargs=None) -> Callable:
    shared_kwargs_str = serialize_kwargs(shared_kwargs)
    if shared_kwargs_str not in self._f_grad:
      self._f_grad[shared_kwargs_str] = self._make_f_grad(shared_kwargs)
    return self._f_grad[shared_kwargs_str]

  def f_loss(self, shared_kwargs=None) -> Callable:
    shared_kwargs_str = serialize_kwargs(shared_kwargs)
    if shared_kwargs_str not in self._f_loss:
      self._f_loss[shared_kwargs_str] = self._make_f_loss(shared_kwargs)
      if self.jit['loss']:
        dyn_vars = self.target.vars()
        dyn_vars.update(self.dyn_vars)
        self._f_loss[shared_kwargs_str] = bm.jit(self._f_loss[shared_kwargs_str],
                                                 dyn_vars=dyn_vars)
    return self._f_loss[shared_kwargs_str]

  def f_train(self, shared_kwargs=None) -> Callable:
    shared_kwargs_str = serialize_kwargs(shared_kwargs)
    if shared_kwargs_str not in self._f_train:
      self._f_train[shared_kwargs_str] = self._make_f_train(shared_kwargs)
    return self._f_train[shared_kwargs_str]

  @property
  def train_losses(self):
    """Training loss."""
    return self._train_losses

  @property
  def test_losses(self):
    """Training loss."""
    return self._test_losses

  @property
  def mapping_type(self):
    """Mapping type for the output and the target."""
    return self._mapping_type

  def _make_f_loss(self, shared_kwargs: Dict = None):
    if shared_kwargs is None: shared_kwargs = dict()
    assert isinstance(shared_kwargs, dict), (f'Only supports dict for "shared_kwargs". '
                                             f'But got {type(shared_kwargs)}: {shared_kwargs}')

    def loss_fun(inputs, targets):
      inputs = self._format_xs(inputs)
      targets = self._format_ys(targets)
      inputs = {k: bm.moveaxis(v, 0, 1) for k, v in inputs.items()}
      outputs, _ = self._predict(xs=inputs, shared_kwargs=shared_kwargs)
      outputs = self._format_ys(outputs)
      loss = 0.
      for key, output in outputs.items():
        if self.mapping_type[key] == MANY2ONE:
          output = output[:, -1]
        loss += self.loss_fun(output, targets[key])
      return loss

    return loss_fun

  def _make_f_grad(self, shared_kwargs: Dict = None):
    _f_loss_internal = self._make_f_loss(shared_kwargs)
    dyn_vars = self.target.vars()
    dyn_vars.update(self.dyn_vars)
    tran_vars = dyn_vars.subset(bm.TrainVar)
    return bm.grad(_f_loss_internal,
                   dyn_vars=dyn_vars.unique(),
                   grad_vars=tran_vars.unique(),
                   return_value=True)

  def _make_f_train(self, shared_kwargs: Dict = None):
    if shared_kwargs is None: shared_kwargs = dict()
    assert isinstance(shared_kwargs, dict), (f'Only supports dict for "shared_kwargs". '
                                             f'But got {type(shared_kwargs)}: {shared_kwargs}')

    def train_func(inputs, targets):
      inputs = self._format_xs(inputs)
      targets = self._format_ys(targets)
      grads, loss = self.f_grad(shared_kwargs)(inputs, targets)
      if self.max_grad_norm is not None:
        check_float(self.max_grad_norm, 'max_grad_norm', min_bound=0.)
        grads = bm.clip_by_norm(grads, self.max_grad_norm)
      self.optimizer.update(grads)
      return loss

    if self.jit['fit']:
      dyn_vars = self.target.vars()
      dyn_vars.update(self.dyn_vars)
      dyn_vars.update(self.optimizer.vars())
      train_func = bm.jit(train_func, dyn_vars=dyn_vars.unique())
    return train_func

  def _format_ys(self, ys):
    if isinstance(ys, (bm.ndarray, jnp.ndarray)):
      if isinstance(self.target, Network):
        assert len(self.target.exit_nodes) == 1, (f'The network {self.target} has '
                                                  f'{len(self.target.exit_nodes)} '
                                                  f'output nodes, while we only got '
                                                  f'one output data.')
        ys = {self.target.exit_nodes[0].name: ys}
      else:
        ys = {self.target.name: ys}
    else:
      for node in self.target.exit_nodes:
        if node.name not in ys:
          raise ValueError(f'The network has output node {node.name}, '
                           f'however, we did not get the corresponding '
                           f'output targets.')
    check_dict_data(ys, key_type=str, val_type=(bm.ndarray, jnp.ndarray))
    return ys

  def _check_mapping_type(self, ys):
    if self.mapping_type is None:
      self._mapping_type = dict()
    for (key, y) in ys.items():
      assert y.ndim in [2, 3], ('Each tensor in "ys" must have the shape of '
                                '(num_sample, num_time, num_feature) or '
                                '(num_sample, num_feature), but we '
                                f'got {y.shape}')
      if key not in self._mapping_type:
        self._mapping_type[key] = MANY2MANY if y.ndim == 3 else MANY2ONE
      else:
        if self._mapping_type[key] != (MANY2MANY if y.ndim == 3 else MANY2ONE):
          raise ValueError(f'Mapping type of {key} is {self.mapping_type[key]}, '
                           f'it cannot be changed.')

  def _get_train_data(self, train_data, num_batch):
    # training dataset
    if callable(train_data):
      train_data = self._get_data_by_method1(train_data, num_batch)
    elif isinstance(train_data, (tuple, list)):
      assert len(train_data) == 2, f"Must be (X, Y) pair, but got a sequence with length {len(train_data)}"
      train_data = self._get_data_by_method2(train_data,
                                             num_batch=num_batch,
                                             shuffle=self.shuffle_data)
    else:
      raise ValueError(f'Train data does not support {type(train_data)}. ')
    return train_data

  def _get_test_data(self, test_data, num_batch):
    # testing dataset
    if test_data is None:
      test_data = None
    elif callable(test_data):
      test_data = self._get_data_by_method1(test_data, num_batch)
    elif isinstance(test_data, (tuple, list)):
      assert len(test_data) == 2, f"Must be (X, Y) pair, but got a sequence with length {len(test_data)}"
      test_data = self._get_data_by_method2(test_data,
                                            num_batch=num_batch,
                                            shuffle=False)
    else:
      raise ValueError(f'Test data does not support {type(test_data)}. ')
    return test_data

  def _get_data_by_method1(self, dataset, num_batch):
    for xs, ys in dataset():
      xs = self._format_xs(xs)
      ys = self._format_ys(ys)
      yield xs, ys

  def _get_data_by_method2(self, dataset, num_batch, shuffle=False, ):
    assert isinstance(dataset, (tuple, list)) and len(dataset) == 2
    xs, ys = dataset
    xs, _, num_sample = self._check_xs(xs, move_axis=False)
    ys = self._format_ys(ys)
    if shuffle:
      seed = np.random.randint(0, 100000)
      xs = tree_map(lambda data: bm.random.RandomState(seed).shuffle(data, axis=0), xs)
      ys = tree_map(lambda data: bm.random.RandomState(seed).shuffle(data, axis=0), ys)

    # def data_iter():
    for data_idx in range(0, num_sample, num_batch):
      if (data_idx + num_batch) > num_sample:
        ids = bm.arange(data_idx, data_idx + num_batch) % num_sample
        inputs = {k: v[ids] for k, v in xs.items()}
        targets = {k: v[ids] for k, v in ys.items()}
      else:
        inputs = {k: v[data_idx: data_idx + num_batch] for k, v in xs.items()}
        targets = {k: v[data_idx: data_idx + num_batch] for k, v in ys.items()}
      yield inputs, targets
