# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""
Lambda Callback
^^^^^^^^^^^^^^^

Create a simple callback on the fly using lambda functions.

"""

from typing import Callable, Optional

from pytorch_lightning.callbacks.base import Callback


class LambdaCallback(Callback):
    r"""
    Create a simple callback on the fly using lambda functions.

    Args:
        **kwargs: hooks supported by :class:`~pytorch_lightning.callbacks.base.Callback`

    Example::

        >>> from pytorch_lightning import Trainer
        >>> from pytorch_lightning.callbacks import LambdaCallback
        >>> trainer = Trainer(callbacks=[LambdaCallback(setup=lambda *args: print('setup'))])
    """

    def __init__(
        self,
        on_before_accelerator_backend_setup: Optional[Callable] = None,
        setup: Optional[Callable] = None,
        on_configure_sharded_model: Optional[Callable] = None,
        teardown: Optional[Callable] = None,
        on_init_start: Optional[Callable] = None,
        on_init_end: Optional[Callable] = None,
        on_fit_start: Optional[Callable] = None,
        on_fit_end: Optional[Callable] = None,
        on_sanity_check_start: Optional[Callable] = None,
        on_sanity_check_end: Optional[Callable] = None,
        on_train_batch_start: Optional[Callable] = None,
        on_train_batch_end: Optional[Callable] = None,
        on_train_epoch_start: Optional[Callable] = None,
        on_train_epoch_end: Optional[Callable] = None,
        on_validation_epoch_start: Optional[Callable] = None,
        on_validation_epoch_end: Optional[Callable] = None,
        on_test_epoch_start: Optional[Callable] = None,
        on_test_epoch_end: Optional[Callable] = None,
        on_epoch_start: Optional[Callable] = None,
        on_epoch_end: Optional[Callable] = None,
        on_batch_start: Optional[Callable] = None,
        on_validation_batch_start: Optional[Callable] = None,
        on_validation_batch_end: Optional[Callable] = None,
        on_test_batch_start: Optional[Callable] = None,
        on_test_batch_end: Optional[Callable] = None,
        on_batch_end: Optional[Callable] = None,
        on_train_start: Optional[Callable] = None,
        on_train_end: Optional[Callable] = None,
        on_pretrain_routine_start: Optional[Callable] = None,
        on_pretrain_routine_end: Optional[Callable] = None,
        on_validation_start: Optional[Callable] = None,
        on_validation_end: Optional[Callable] = None,
        on_test_start: Optional[Callable] = None,
        on_test_end: Optional[Callable] = None,
        on_keyboard_interrupt: Optional[Callable] = None,
        on_exception: Optional[Callable] = None,
        on_save_checkpoint: Optional[Callable] = None,
        on_load_checkpoint: Optional[Callable] = None,
        on_before_backward: Optional[Callable] = None,
        on_after_backward: Optional[Callable] = None,
        on_before_optimizer_step: Optional[Callable] = None,
        on_before_zero_grad: Optional[Callable] = None,
        on_predict_start: Optional[Callable] = None,
        on_predict_end: Optional[Callable] = None,
        on_predict_batch_start: Optional[Callable] = None,
        on_predict_batch_end: Optional[Callable] = None,
        on_predict_epoch_start: Optional[Callable] = None,
        on_predict_epoch_end: Optional[Callable] = None,
    ):
        for k, v in locals().items():
            if k == "self":
                continue
            if v is not None:
                setattr(self, k, v)
