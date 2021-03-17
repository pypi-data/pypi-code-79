# -*- coding: utf-8 -*-

'''
    Demo model in wxbtool package

    This model predict t850 3-days in the future
    The performance is relative weak, but it can be easily fitted into one normal gpu
    the weighted rmse is 2.62 K
'''

import torch as th
import torch.nn as nn

from leibniz.nn.net import resunet
from leibniz.nn.activation import CappingRelu
from leibniz.unet.senet import SEBottleneck

from wxbtool.specs.t850 import Spec, Setting3d


class Enhencer(nn.Module):
    def __init__(self, channels):
        super(Enhencer, self).__init__()
        hidden = channels * 2
        self.fci = nn.Linear(channels, hidden)
        self.fco = nn.Linear(hidden, channels)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        b, c, h, w = x.size()
        out = self.fci(x.view(b, c * h * w))
        out = self.relu(out)
        out = self.fco(out).view(b, c, h, w)
        return out


class ResUNetModel(Spec):
    def __init__(self, setting):
        super().__init__(setting)
        self.name = 't850'

        enhencer = Enhencer(3328)
        self.resunet = resunet(setting.input_span * (len(setting.vars) + 2) + self.constant_size + 2, 1,
                            spatial=(32, 64+2), layers=5, ratio=-1,
                            vblks=[2, 2, 2, 2, 2], hblks=[1, 1, 1, 1, 1],
                            scales=[-1, -1, -1, -1, -1], factors=[1, 1, 1, 1, 1],
                            block=SEBottleneck, relu=CappingRelu(), enhencer=enhencer,
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
