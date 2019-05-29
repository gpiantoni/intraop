from .paths import (
    MOUTH_FUNC,
    MOUTH_FMAP,
    NIPYPE_PATH,
    )
from intraop.fmri.workflows.topup import make_w_topup


def test_topup():
    w = make_w_topup()
    w.base_dir = str(NIPYPE_PATH)

    node = w.get_node('input')
    node.inputs.func = str(MOUTH_FUNC)  # this should be after motion correction
    node.inputs.fmap = str(MOUTH_FMAP)

    w.write_graph(graph2use='flat')
    w.write_graph(graph2use='colored')

    w.run(plugin='MultiProc')
