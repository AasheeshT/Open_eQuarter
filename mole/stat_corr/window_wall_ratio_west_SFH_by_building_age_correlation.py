# OeQ autogenerated correlation for 'Window/Wall Ratio West in Correlation to the Building Age'

import math
import numpy as np
import oeqCorrelation as oeq
def window_wall_ratio_west_SFH_by_building_age_correlation(*xin):

    # OeQ autogenerated correlation for 'Window to Wall Ratio in Western Direction'
    A_WIN_W_BY_AW= oeq.correlation(
    const= 3443.04500822,
    a=     -7.03961089554,
    b=     0.00539428257241,
    c=     -1.83599645651e-06,
    d=     2.34190543055e-10,
    mode= "lin")

    return dict(A_WIN_W_BY_AW=A_WIN_W_BY_AW.lookup(*xin))
