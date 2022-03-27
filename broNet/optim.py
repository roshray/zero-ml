#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 roshan <roshan@roshan-ThinkPad-T440p>
#
# Distributed under terms of the MIT license.

"""
optimizer : to adjust the parameters of our network 
            based on the gradients 
            computed during propogation

"""
from broNet.nn import NeuralNet

class Optimizer:
    def step(self, net: NeuralNet) -> None:
        raise NotImplmentedError










