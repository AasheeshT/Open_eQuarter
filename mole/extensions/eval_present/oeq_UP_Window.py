# -*- coding: utf-8 -*-

import os,math
from qgis.core import NULL
from mole import oeq_global
from mole.project import config
from mole.extensions import OeQExtension
from mole.stat_corr import rb_present_window_uvalue_AVG_by_building_age_lookup, nrb_present_window_uvalue_by_building_age_lookup

def calculation(self=None, parameters={},feature = None):
    from scipy.constants import golden
    from math import floor, ceil
    from PyQt4.QtCore import QVariant
    wn_up = NULL

#differentiation between RB and NRB (for now in case of contemporary U-Values RB=NRB. After getting NRB data for contemporary case code must be adaptet)
    if parameters['BLD_USAGE'] == "RB":
        if not oeq_global.isnull(parameters['YOC']):
            wn_up = rb_present_window_uvalue_AVG_by_building_age_lookup.get(parameters['YOC'])

    elif parameters['BLD_USAGE'] == "NRB":
        if not oeq_global.isnull(parameters['YOC']):
            wn_up=nrb_present_window_uvalue_by_building_age_lookup.get(parameters['YOC'])

    else:
        if not oeq_global.isnull(parameters['YOC']):
            wn_up=(((rb_present_window_uvalue_AVG_by_building_age_lookup.get(parameters['YOC'])) + (nrb_present_window_uvalue_by_building_age_lookup.get(parameters['YOC']))) / 2)

    return {'WN_UP': {'type': QVariant.Double, 'value': wn_up}}

extension = OeQExtension(
    extension_id=__name__,

    category='Evaluation',
    subcategory='U-Values Present',
    extension_name='Window Quality (U_Value, Present)',
    layer_name= 'U Window Present',
    extension_filepath=os.path.join(__file__),
    colortable = os.path.join(os.path.splitext(__file__)[0] + '.qml'),
    field_id='WN_UP',
    source_type='none',
    par_in=['YOC','BLD_USAGE'],
    sourcelayer_name=config.data_layer_name,
    targetlayer_name=config.data_layer_name,
    active=True,
    show_results=['WN_UP'],
    description=u"Calculate the present U-Value of the Building's windoes",
    evaluation_method=calculation)

extension.registerExtension(default=True)
