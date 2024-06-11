# Copyright (c) DarwinCloud LLC. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from pathlib import Path

import pytest
from prtm import protein
from prtm.models.esm import modeling

from ..test_utils import _compare_structures

