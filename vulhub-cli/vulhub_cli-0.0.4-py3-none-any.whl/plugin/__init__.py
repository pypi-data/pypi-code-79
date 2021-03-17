#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: owefsad@huoxian.cn
# datetime: 2021/3/17 下午12:09
# project: vulhub-compose


class BasePlugin(object):
    def attach(self, yaml_file):
        pass

    def detach(self, yaml_file):
        pass
