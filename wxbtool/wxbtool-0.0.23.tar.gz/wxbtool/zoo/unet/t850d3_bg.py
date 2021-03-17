# -*- coding: utf-8 -*-

'''
    Demo model in wxbtool package

    This model predict t850 3-days in the future
    it cost more memory and can be fitted into one P40 gpu at batch size 64
    the weighted rmse is 2.23 K
'''

import torch as th

from leibniz.nn.activation import CappingRelu
from leibniz.nn.net import resunet, hyptub, linear
from leibniz.unet.hyperbolic import HyperBottleneck

from wxbtool.specs.t850 import Spec, Setting3d


class ResUNetModel(Spec):
    def __init__(self, setting):
        super().__init__(setting)
        self.name = 't850bg'

        enhencer = hyptub(1408, 704, 1408, encoder=linear, decoder=linear)
        self.resunet = resunet(setting.input_span * (len(setting.vars) + 2) + self.constant_size + 2, 1,
                            spatial=(32, 64+2), layers=5, ratio=-1,
                            vblks=[2, 2, 2, 2, 2], hblks=[1, 1, 1, 1, 1],
                            scales=[-1, -1, -1, -1, -1], factors=[1, 1, 1, 1, 1],
                            block=HyperBottleneck, relu=CappingRelu(), enhencer=enhencer,
                            final_normalized=False)

    def forward(self, **kwargs):
        batch_size = kwargs['temperature'].size()[0]
        self.update_da_status(batch_size)

        _, input = self.get_inputs(**kwargs)
        constant = self.get_augmented_constant(input)
        input = th.cat((input, constant), dim=1)
        input = th.cat((input[:, :, :, 63:64], input, input[:, :, :, 0:1]), dim=3)

        output = self.resunet(input)

        output = output[:, :, :, 1:65]
        return {
            't850': output
        }


setting = Setting3d()
model = ResUNetModel(setting)
