# -*- coding: utf-8 -*-

import os,math
from qgis.core import NULL
from mole import oeq_global
from mole.project import config
from mole.extensions import OeQExtension
from mole.stat_corr import contemporary_base_uvalue_by_building_age_lookup

def calculation(self=None, parameters={},feature = None):
    from scipy.constants import golden
    from math import floor, ceil
    from PyQt4.QtCore import QVariant
    # factor for golden rule
    dataset = {'BS_SQTC': NULL}
    dataset.update(parameters)

    if not oeq_global.isnull([dataset['BS_UC'],dataset['HHRS']]):
        dataset['BS_SQTC']=float(dataset['BS_UC'])*float(dataset['HHRS'])/1000*0.35 #correction factor

    result = {}
    for i in dataset.keys():
        result.update({i: {'type': QVariant.Double,
                           'value': dataset[i]}})
    return result


extension = OeQExtension(
    extension_id=__name__,

    category='Evaluation',
    subcategory='Contemp. Spec. Transm. Heat Loss',
    extension_name='Base SpecTransm (SQT, Contemporary)',
    layer_name= 'SQT Base Contemporary',
    extension_filepath=os.path.join(__file__),
    colortable = os.path.join(os.path.splitext(__file__)[0] + '.qml'),
    field_id='BS_SQTC',
    source_type='none',
    par_in=['BS_UC','HHRS'],
    sourcelayer_name=config.data_layer_name,
    targetlayer_name=config.data_layer_name,
    active=True,
    show_results=['BS_SQTC'],
    description=u"Calculate the contemporary Transmission Heat Loss of the Building's baseplate per m2",
    evaluation_method=calculation)

extension.registerExtension(default=True)
