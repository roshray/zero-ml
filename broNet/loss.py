#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 roshan <roshan@roshan-ThinkPad-T440p>
#
# Distributed under terms of the MIT license.

"""
Loss Function :
    MSE :
"""
import numpy as np
from broNet.tensor import Tensor


class Loss:
    def loss(self,predicted: Tensor,actual: Tensor) -> float:
        raise NotImplementedError

    def grad(self, predicted: Tensor, actual:Tensor) -> Tensor:
        raise NotImplementedError



class MSE(Loss):
    def loss(self,predicted: Tensor,actual: Tensor) -> float:
       return np.sum((predicted - actual) ** 2)    

    def grad(self, predicted: Tensor, actual:Tensor) -> Tensor:
        return 2 * (predicted - actual)

