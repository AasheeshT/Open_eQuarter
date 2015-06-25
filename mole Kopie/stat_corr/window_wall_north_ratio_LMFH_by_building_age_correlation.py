# OeQ autogenerated correlation for 'Window/Wall Ratio North in Correlation to the Building Age'

import math
import numpy as np
import oeqCorrelation as oeq
def window_wall_north_ratio_LMFH_by_building_age_correlation(*xin):

    # OeQ autogenerated correlation for 'Window to Wall Ratio in Northern Direction'
    A_WIN_N_BY_AW= oeq.correlation(
    const= -16855.7432878,
    a=     34.8833074263,
    b=     -0.027056163872,
    c=     9.32124051088e-06,
    d=     -1.20350325915e-09,
    mode= "lin")

    return dict(A_WIN_N_BY_AW=A_WIN_N_BY_AW.lookup(*xin))

