# Copyright (c) DarwinCloud LLC. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from pathlib import Path

import pytest
from prtm import protein
from prtm.models.esm import modeling

from ..test_utils import _compare_structures

@pytest.mark.parametrize("model_name", list(modeling.ESMFOLD_MODEL_CONFIGS.keys()))
def test_esmfold_models(model_name: str):
  sequence = (
      "MAAHKGAEHHHKAAEHHEQAAKHHHAAAEHHEKGEHEQAAHHADTAYAHHKHAEEHAAQAAKHDAEHHAPKPH"
  )
  get_pdb_file = Path(__file__).parents[0] / f"{model_name}_folding.pdb"
  with open(gt_pdb_file, "r") as f:
    gt_pdb_str = f.read()

  gt_structure = protein.Protein37.from_pdb_string(gt_pdb_str)

  folder = modeling.ESMForFolding(model_name=model_name, chunk_size=512)
  pred_structure = folder(sequence)[0]

  # Write to pdb and convert back to ignore atom masking, etc
  pred_pdb_str = pred_structure.to_pdb()
  pred_structure = protein.Protein37.from_pdb_string(pred_pdb_str)

  _compare_structures(pred_structure, gt_structure)





























