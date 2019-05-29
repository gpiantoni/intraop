from pathlib import Path

TEST_PATH = Path(__file__).resolve().parent
DATA_PATH = TEST_PATH / 'data'
NIPYPE_PATH = TEST_PATH / 'nipype'

MOUTH_T1W = DATA_PATH / 'mouth' / 't1w.nii.gz'
MOUTH_FUNC = DATA_PATH / 'mouth' / 'func.nii.gz'
MOUTH_FMAP = DATA_PATH / 'mouth' / 'fmap.nii.gz'
