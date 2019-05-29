
from nipype import Function


def wrapper_acqparams(in_file, output_dir='.'):

    from pathlib import Path
    from nibabel import load

    nii = load(in_file)
    n_dyn = nii.shape[3]

    file_acqparam = Path(output_dir).resolve() / 'acquisition_parameters.txt'
    with file_acqparam.open('w') as f:
        for i in range(n_dyn):
            f.write('0 -1 0 1\n')

    return str(file_acqparam)


function_acq_params = Function(
    input_names=[
        'in_file',
    ],
    output_names=[
        'encoding_file',
    ],
    function=wrapper_acqparams,
    )
