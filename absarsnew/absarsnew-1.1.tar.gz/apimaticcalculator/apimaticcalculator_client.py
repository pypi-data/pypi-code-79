# -*- coding: utf-8 -*-

"""
apimaticcalculator

This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from apimaticcalculator.decorators import lazy_property
from apimaticcalculator.configuration import Configuration
from apimaticcalculator.configuration import Environment
from apimaticcalculator.controllers.simple_calculator_controller\
    import SimpleCalculatorController


class ApimaticcalculatorClient(object):

    @lazy_property
    def simple_calculator(self):
        return SimpleCalculatorController(self.config)

    def __init__(self, timeout=60, max_retries=3, backoff_factor=0,
                 environment=Environment.PRODUCTION, config=None):
        if config is None:
            self.config = Configuration(timeout=timeout,
                                        max_retries=max_retries,
                                        backoff_factor=backoff_factor,
                                        environment=environment)
        else:
            self.config = config
