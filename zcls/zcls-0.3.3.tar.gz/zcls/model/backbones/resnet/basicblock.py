# -*- coding: utf-8 -*-

"""
@date: 2020/11/21 下午2:38
@file: basicblock.py
@author: zj
@description: 
"""
from abc import ABC

import torch.nn as nn

from zcls.model.attention_helper import make_attention_block


class BasicBlock(nn.Module, ABC):
    expansion = 1

    def __init__(self,
                 in_channels,
                 out_channels,
                 stride=1,
                 downsample=None,
                 groups=1,
                 base_width=64,
                 with_attention=False,
                 reduction=16,
                 attention_type='SqueezeAndExcitationBlock2D',
                 conv_layer=None,
                 norm_layer=None,
                 act_layer=None,
                 **kwargs
                 ):
        """
        使用两个3x3卷积，如果进行下采样，那么使用第一个卷积层对输入空间尺寸进行减半操作
        参考Torchvision实现
        对于注意力模块，有两种嵌入方式：
        1. 对于Squeeze-And-Excitation或者Global Context操作，在残差连接中（after 1x1）嵌入；
        2. 对于NonLocal或者SimplifiedNonLoal，在Block完成计算后（after add）嵌入。
        :param in_channels:　输入通道数
        :param out_channels:　输出通道数
        :param stride:　步长
        :param downsample:　下采样
        :param groups:　cardinality
        :param base_width:　基础宽度
        :param with_attention:　是否使用注意力模块
        :param reduction:　衰减率
        :param attention_type:　注意力模块类型
        :param conv_layer:　卷积层类型
        :param norm_layer:　归一化层类型
        :param act_layer:　激活层类型
        :param kwargs:　其他参数
        """
        super(BasicBlock, self).__init__()
        assert with_attention in (0, 1)
        assert attention_type in ['GlobalContextBlock2D',
                                  'SimplifiedNonLocal2DEmbeddedGaussian',
                                  'NonLocal2DEmbeddedGaussian',
                                  'SqueezeAndExcitationBlock2D']
        if groups != 1 or base_width != 64:
            raise ValueError('BasicBlock only supports groups=1 and base_width=64')

        if conv_layer is None:
            conv_layer = nn.Conv2d
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        if act_layer is None:
            act_layer = nn.ReLU

        self.down_sample = downsample

        self.conv1 = conv_layer(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = norm_layer(out_channels)

        self.conv2 = conv_layer(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = norm_layer(out_channels)

        self.relu = act_layer(inplace=True)

        self.attention_after_1x1 = None
        self.attention_after_add = None
        if with_attention and attention_type in ['SqueezeAndExcitationBlock2D', 'GlobalContextBlock2D']:
            self.attention_after_1x1 = make_attention_block(out_channels * self.expansion, reduction, attention_type)
            self.attention_after_add = None
        if with_attention and attention_type in ['NonLocal2DEmbeddedGaussian', 'SimplifiedNonLocal2DEmbeddedGaussian']:
            self.attention_after_1x1 = None
            self.attention_after_add = make_attention_block(out_channels * self.expansion, reduction, attention_type)

    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.attention_after_1x1 is not None:
            out = self.attention_after_1x1(out)

        if self.down_sample is not None:
            identity = self.down_sample(x)

        out += identity
        out = self.relu(out)

        if self.attention_after_add is not None:
            out = self.attention_after_add(out)

        return out
