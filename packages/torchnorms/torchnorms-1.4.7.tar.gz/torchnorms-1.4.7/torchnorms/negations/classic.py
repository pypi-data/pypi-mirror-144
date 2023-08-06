# -*- coding: utf-8 -*-

import torch
from torch import Tensor
from torchnorms.negations.base import BaseNegation


class StandardNegation(BaseNegation):
    def __init__(self) -> None:
        super().__init__()
        self.__name__ = 'standard'

    @classmethod
    def __call__(cls,
                 a: Tensor) -> Tensor:
        return 1.0 - a


class StrictNegation(BaseNegation):
    def __init__(self) -> None:
        super().__init__()
        self.__name__ = 'strict'

    @classmethod
    def __call__(cls,
                 a: Tensor) -> Tensor:
        return 1.0 - torch.pow(a, 2)


class StrictCosNegation(BaseNegation):
    def __init__(self) -> None:
        super().__init__()
        self.__name__ = 'strict_cosine'

    @classmethod
    def __call__(cls,
                 a: Tensor) -> Tensor:
        pi = torch.acos(torch.zeros(1)).item() * 2
        res = 0.5 * (torch.cos(pi * a))
        return res
