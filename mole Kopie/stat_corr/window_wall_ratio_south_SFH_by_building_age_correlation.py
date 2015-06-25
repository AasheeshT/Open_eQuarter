# OeQ autogenerated correlation for 'Window/Wall Ratio South in Correlation to the Building Age'

import math
import numpy as np
import oeqCorrelation as oeq
def get(*xin):

    # OeQ autogenerated correlation for 'Window to Wall Ratio in Southern Direction'
    A_WIN_S_BY_AW= oeq.correlation(
    const= 9428.07222626,
    a=     -19.2068359893,
    b=     0.0146645925133,
    c=     -4.97344110344e-06,
    d=     6.32178163644e-10,
    mode= "lin")

    return dict(A_WIN_S_BY_AW=A_WIN_S_BY_AW.lookup(*xin))

