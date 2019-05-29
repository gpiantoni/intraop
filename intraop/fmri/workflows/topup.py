from tempfile import mkstemp
from os import fdopen
from nipype.pipeline.engine import Node, Workflow
from nipype.interfaces.utility import IdentityInterface
from nipype.interfaces.utility import Merge as Merge_list
from nipype.interfaces.fsl import MCFLIRT, Merge, TOPUP, ApplyTOPUP, MeanImage

from .utils import function_acq_params


def make_w_topup():
    n_in = Node(IdentityInterface(fields=[
        'func',  # after motion correction
        'fmap',
        ]), name='input')

    n_out = Node(IdentityInterface(fields=[
        'func',
        ]), name='output')

    n_mean_func = Node(MeanImage(), name='mean_func')

    n_mc_fmap = Node(MCFLIRT(), name='motion_correction_fmap')
    n_mean_fmap = Node(MeanImage(), name='mean_fmap')

    n_list = Node(Merge_list(2), name='list')
    n_merge = Node(Merge(), name='merge')
    n_merge.inputs.dimension = 't'

    n_topup = Node(TOPUP(), name='topup')
    n_topup.inputs.encoding_file = _generate_acqparams()
    n_topup.inputs.subsamp = 1  # slower, but it accounts for odd number of slices

    n_acqparam = Node(function_acq_params, name='acquisition_parameters')

    n_apply = Node(ApplyTOPUP(), name='topup_apply')
    n_apply.inputs.method = 'jac'

    w = Workflow('topup')
    w.connect(n_in, 'fmap', n_mc_fmap, 'in_file')
    w.connect(n_mc_fmap, 'out_file', n_mean_fmap, 'in_file')
    w.connect(n_in, 'func', n_mean_func, 'in_file')
    w.connect(n_mean_func, 'out_file', n_list, 'in1')
    w.connect(n_mean_fmap, 'out_file', n_list, 'in2')
    w.connect(n_list, 'out', n_merge, 'in_files')
    w.connect(n_merge, 'merged_file', n_topup, 'in_file')

    w.connect(n_in, 'func', n_apply, 'in_files')
    w.connect(n_topup, 'out_fieldcoef', n_apply, 'in_topup_fieldcoef')
    w.connect(n_topup, 'out_movpar', n_apply, 'in_topup_movpar')
    w.connect(n_in, 'func', n_acqparam, 'in_file')
    w.connect(n_acqparam, 'encoding_file', n_apply, 'encoding_file')

    w.connect(n_apply, 'out_corrected', n_out, 'func')

    return w


def _generate_acqparams():
    i, acq_params = mkstemp(suffix='.txt')
    with fdopen(i, 'w') as f:
        f.write('0 -1 0 1\n')
        f.write('0 1 0 1\n')

    return acq_params
