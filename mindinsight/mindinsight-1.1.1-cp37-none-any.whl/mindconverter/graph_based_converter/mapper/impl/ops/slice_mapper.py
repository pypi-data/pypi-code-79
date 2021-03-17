# Copyright 2020 Huawei Technologies Co., Ltd.All Rights Reserved.
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
# ==============================================================================
"""Mapper module."""
from ...base import ONNXToMindSporeMapper
from ...gen_setting import Setting


class SliceMapper(ONNXToMindSporeMapper):
    """Slice mapper."""

    @staticmethod
    def _operation_name_in_ms(*args, **kwargs):
        return "P.Slice"

    @staticmethod
    def _convert_params(**kwargs):
        return dict()

    @staticmethod
    def _convert_trained_weights(**kwargs):
        return dict()

    @staticmethod
    def _convert_settings(**kwargs):
        weights = list(kwargs.get("weights").values())  # start, end, axis
        opt_shape = kwargs["params"].get("output_shape")
        if not weights:
            raise ValueError("Cannot get required params from slice.")
        starts = sorted(zip(weights[0].tolist(), weights[2].tolist()), key=lambda x: x[1], reverse=False)
        return Setting(op_extra_input={"begin": tuple([i[0] for i in starts]),
                                       "size": tuple(opt_shape)})
