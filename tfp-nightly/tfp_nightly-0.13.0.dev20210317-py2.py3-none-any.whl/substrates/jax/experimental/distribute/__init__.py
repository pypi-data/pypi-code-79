# Copyright 2020 The TensorFlow Probability Authors.
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
# ============================================================================
"""Experimental module for doing distributed log prob calculations."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_probability.substrates.jax.experimental.distribute.distribute_lib import make_sharded_log_prob_parts
from tensorflow_probability.substrates.jax.experimental.distribute.joint_distribution import JointDistributionCoroutine
from tensorflow_probability.substrates.jax.experimental.distribute.joint_distribution import JointDistributionNamed
from tensorflow_probability.substrates.jax.experimental.distribute.joint_distribution import JointDistributionSequential
from tensorflow_probability.substrates.jax.experimental.distribute.sharded import Sharded

__all__ = [
    'JointDistributionCoroutine',
    'JointDistributionNamed',
    'JointDistributionSequential',
    'make_sharded_log_prob_parts',
    'Sharded',
]

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# This file is auto-generated by substrates/meta/rewrite.py
# It will be surfaced by the build system as a symlink at:
#   `tensorflow_probability/substrates/jax/experimental/distribute/__init__.py`
# For more info, see substrate_runfiles_symlinks in build_defs.bzl
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# (This notice adds 10 to line numbering.)


