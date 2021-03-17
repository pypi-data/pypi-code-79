# PyAlgoTrade
#
# Copyright 2011-2018 Gabriel Martin Becedillas Ruiz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: Gabriel Martin Becedillas Ruiz <gabriel.becedillas@gmail.com>
"""

from pyalgotrade import technical
from pyalgotrade.dataseries import bards
#lw加的
from pyalgotrade import commonHelpBylw

# This event window will calculate and hold true-range values.
# Formula from http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_true_range_atr.
class ATREventWindow(technical.EventWindow):
    def __init__(self, period, useAdjustedValues):
        assert(period > 1)
        super(ATREventWindow, self).__init__(period)
        self.__useAdjustedValues = useAdjustedValues
        self.__prevClose = None
        self.__value = None

    def _calculateTrueRange(self, value):
        ret = None
        if self.__prevClose is None:
            ret = value.getHigh(self.__useAdjustedValues) - value.getLow(self.__useAdjustedValues)
        else:
            tr1 = value.getHigh(self.__useAdjustedValues) - value.getLow(self.__useAdjustedValues)
            tr2 = abs(value.getHigh(self.__useAdjustedValues) - self.__prevClose)
            tr3 = abs(value.getLow(self.__useAdjustedValues) - self.__prevClose)
            ret = max(max(tr1, tr2), tr3)
        return ret

    def onNewValue(self, dateTime, value):
        tr = self._calculateTrueRange(value)
        super(ATREventWindow, self).onNewValue(dateTime, tr)
        self.__prevClose = value.getClose(self.__useAdjustedValues)

        if value is not None and self.windowFull():
            if self.__value is None:
                self.__value = self.getValues().mean()
            else:
                #lw的注释，这算法，是一次指数平滑的公式，不是简单平均
                self.__value = (self.__value * (self.getWindowSize() - 1) + tr) / float(self.getWindowSize())

    def getValue(self):
        return self.__value


#这个函数是lw李文补得。用来提供 简单平均的方式 计算atr
class ATRSmaEventWindow(technical.EventWindow):
    def __init__(self, period, useAdjustedValues):
        # 这里原作者觉得atr至少要过去2个bar才能算。我查了下面tr的算法，发现只有一个bar的时候
        # 也计算出了tr，那么一个bar，能有tr，那么也必然可以有atr
        # assert(period > 1)
        super(ATRSmaEventWindow, self).__init__(period)
        self.__useAdjustedValues = useAdjustedValues
        self.__prevClose = None
        self.__value = None

    def _calculateTrueRange(self, value):
        ret = None
        if self.__prevClose is None:
            ret = value.getHigh(self.__useAdjustedValues) - value.getLow(self.__useAdjustedValues)
        else:
            tr1 = value.getHigh(self.__useAdjustedValues) - value.getLow(self.__useAdjustedValues)
            tr2 = abs(value.getHigh(self.__useAdjustedValues) - self.__prevClose)
            tr3 = abs(value.getLow(self.__useAdjustedValues) - self.__prevClose)
            ret = max(max(tr1, tr2), tr3)
        return ret

    def onNewValue(self, dateTime, value):
        tr = self._calculateTrueRange(value)
        super(ATRSmaEventWindow, self).onNewValue(dateTime, tr)
        self.__prevClose = value.getClose(self.__useAdjustedValues)

        if value is not None and self.windowFull():

            self.__value = commonHelpBylw.round_up(self.getValues().mean(),2) #简单平均



    def getValue(self):
        return self.__value





class ATR(technical.EventBasedFilter):
    """Average True Range filter as described in http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_true_range_atr

    :param barDataSeries: The BarDataSeries instance being filtered.
    :type barDataSeries: :class:`pyalgotrade.dataseries.bards.BarDataSeries`.
    :param period: The average period. Must be > 1.
    :type period: int.
    :param useAdjustedValues: True to use adjusted Low/High/Close values.
    :type useAdjustedValues: boolean.
    :param maxLen: The maximum number of values to hold.
        Once a bounded length is full, when new items are added, a corresponding number of items are discarded from the
        opposite end. If None then dataseries.DEFAULT_MAX_LEN is used.
    :type maxLen: int.
    """

    # def __init__(self, barDataSeries, period, useAdjustedValues=False, maxLen=None):
    #     if not isinstance(barDataSeries, bards.BarDataSeries):
    #         raise Exception("barDataSeries must be a dataseries.bards.BarDataSeries instance")
    #
    #     super(ATR, self).__init__(barDataSeries, ATREventWindow(period, useAdjustedValues), maxLen)
    #

     #lw 要修改代码，将原始代码注释在上面。

    def __init__(self, barDataSeries, period, useAdjustedValues=False, maxLen=None,type='sma'):
        if not isinstance(barDataSeries, bards.BarDataSeries):
            raise Exception("barDataSeries must be a dataseries.bards.BarDataSeries instance")

        if type=='sma':
            awindow=ATRSmaEventWindow(period, useAdjustedValues)
        if type=='ema':
            awindow = ATREventWindow(period, useAdjustedValues)

        super(ATR, self).__init__(barDataSeries, awindow, maxLen)
