from qgis.core import QgsVectorLayer, QgsRasterLayer, QgsCoordinateReferenceSystem, QgsVectorFileWriter, QgsMapLayerRegistry, QgsMapLayer, QGis, QgsProject, QgsFeature
from PyQt4.QtCore import QSettings
import os, time

def create_temporary_layer(layer_name, layer_type, crs_name=''):
    """
    Create and add a new Vectorlayer, with name and type as specified in layer_name, layer_tpye and crs_name
    :param layer_name: The name of the new vectorlayer
    :type layer_name: str
    :param layer_type: The type of the new vectorlayer
    :type layer_type: str
    :param crs_name: The name of the new crs, if empty, the user will be prompted for the crs
    :tpye crs_name: str
    :return The created layer:
    :rtype QgsVectorLayer:
    """
    if layer_name and not layer_name.isspace() and layer_type and not layer_type.isspace():

        crs = ''

        if crs_name and not crs_name.isspace() and QgsCoordinateReferenceSystem().createFromUserInput(crs_name):
            # surpress crs-choice dialog
            old_validation = str(QSettings().value('/Projections/defaultBehaviour', 'prompt'))
            QSettings().setValue('/Projections/defaultBehaviour', 'useProject')
            crs += '?crs=' + crs_name
        else:
            old_validation = str(QSettings().value('/Projections/defaultBehaviour', 'prompt'))
            QSettings().setValue('/Projections/defaultBehaviour', 'prompt')

        # create a new shape-file called layer_name, of the type layer_type, with system encoding and crs according to crs_name
        shape_layer = QgsVectorLayer(layer_type + crs, layer_name, 'memory', False)
        shape_layer.setProviderEncoding('System')

        # reset appearance of crs-choice dialog to previous settings
        QSettings().setValue('/Projections/defaultBehaviour', old_validation)

        return shape_layer

    else:
        return None


def add_style_to_layer(path_to_style, layer):
    """
    Set the style of the layer to the given style
    :param path_to_style:
    :type path_to_style:
    :param layer:
    :type layer:
    :return:
    :rtype:
    """
    if layer and path_to_style and os.path.exists(path_to_style):
        layer.loadNamedStyle(path_to_style)


def add_layer_to_registry(layer):
    """
    Add the given layer to the MapLayerRegistry
    :param layer:
    :type layer:
    :return:
    :rtype:
    """
    if layer:
        # add the layer to the layer-legend
        QgsMapLayerRegistry.instance().addMapLayer(layer)


def find_layer_by_name(layer_name):
    """
    Iterate over all layers and return the layer with the name layer_name, if found
    :param layer_name: Name of the layer that shall be looked for
    :type layer_name: str
    :return:
    :rtype:
    """
    if layer_name and not layer_name.isspace():

        found_layers = QgsMapLayerRegistry.instance().mapLayersByName(layer_name)
        if found_layers != [] and found_layers[0].name() == layer_name:
            return found_layers[0]
        else:
            return None


def hide_or_remove_layer(layer_name, mode='hide', iface = None):
    """
    Hide or remove the given layer from the MapLayerRegistry, depending on the mode.
    :param layer_name: Name of the layer to remove/hide
    :type layer_name: str
    :param mode: What to do with the layer; valid arguments are 'hide' or 'remove'
    :type mode: str
    :return:
    :rtype:
    """
    layer = find_layer_by_name(layer_name)
    if layer and mode == 'remove':
        QgsMapLayerRegistry.instance().removeMapLayer(layer.id())

    if layer and mode == 'hide' and iface:
        iface.legendInterface().setLayerVisible(layer, False)

#ToDo Try to use the currently recommended way to save the layer
def write_vector_layer_to_disk(vlayer, full_path):
    """
    Write the given vector layer to disk.
    :param vlayer: The vector layer that shall be written to disk
    :type vlayer: QgsVectorLayer
    :param full_path: The path and filename the layer shall be written to
    :type full_path: str
    :return:
    :rtype:
    """
    out_path, out_name = os.path.split(full_path)

    if out_name.upper().endswith('.SHP'):
        out_name = out_name[:-4]

    if vlayer is not None and vlayer.isValid() and os.path.exists(out_path):

        if os.path.exists(os.path.join(out_path, out_name + '.shp')):
            new_name = out_name
            suffix = 0

            while os.path.exists(os.path.join(out_path, new_name + '.shp')):
                suffix += 1
                new_name = out_name + str(suffix)

            out_name = new_name

        full_path = os.path.join(out_path, out_name + '.shp')

        provider = vlayer.dataProvider()
        encoding = provider.encoding()
        fields = provider.fields()
        crs = provider.crs()
        writer = QgsVectorFileWriter(full_path, encoding, fields, QGis.WKBPolygon, crs, 'ESRI Shapefile')

        if writer.hasError() != QgsVectorFileWriter.NoError:
            raise IOError('Can\'t create the file: {0}'.format(layer_path))
            del writer
            return None
        else:
            # features = provider.getFeatures()
            # for feature in features:
            #     writer.addFeature(feature)
            #
            # del writer

            out_feat = QgsFeature()
            in_feat = QgsFeature()
            for feat in provider.getFeatures():
                geometry = feat.geometry() # grab it's geometry
                buffer = geometry.buffer(100,10) # buffer the geometry
                out_feat.setAttributes(in_feat.attributes()) # set the attributes for the output feature
                out_feat.setGeometry(buffer) # set the bufer as the output geometry
                writer.addFeature(out_feat) # write the feature to file
            
            timeout = 30
            while not os.path.exists(full_path) and timeout:
                time.sleep(0.1)
                timeout -= 1

            disk_layer = QgsVectorLayer(full_path, out_name, 'ogr')
            
            if disk_layer.isValid():
                return disk_layer
            else:
                return None

    else:
        return None


def trigger_edit_mode(iface, layer_name, trigger='on'):
    """
    Iterate over all layers and activate the Layer called layer_name. Then toggle the edit mode of that layer.
    :param iface: The Qgis-interface that will be accessed
    :type iface: QgisInterface
    :param layer_name: Name of the layer, that shall be switched to edit_mode
    :type layer_name: str
    :return:
    :rtype:
    """
    if layer_name and not layer_name.isspace():

        edit_layer = find_layer_by_name(layer_name)

        # if the layer was found, it is activated and the editing and the adding of features will be triggered
        if edit_layer is not None:

            if trigger == 'on':
                edit_layer.startEditing()
                iface.actionAddFeature().trigger()
            elif trigger == 'off':
                iface.actionAddFeature().trigger()
                edit_layer.commitChanges()


def get_wms_layer_list(iface, visibility='all'):
    """
    Iterate over all layers and return a list of the currently visible WMS-files.
    :param iface: The Qgis-interface that will be accessed
    :type iface: QgisInterface
    :return: A list containing raster layers with the given visibility-value
    :rtype: list
    """
    active_wms_layers = []
    layer_list = QgsMapLayerRegistry.instance().mapLayers()
    interface = iface.legendInterface()

    if visibility == 'visible':
        for key, layer in layer_list.iteritems():
            if layer.type() == QgsMapLayer.RasterLayer and interface.isLayerVisible(layer):
                active_wms_layers.append(layer)

        return active_wms_layers

    elif visibility == 'invisible':
        for key, layer in layer_list.iteritems():
            if layer.type() == QgsMapLayer.RasterLayer and not interface.isLayerVisible(layer):
                active_wms_layers.append(layer)

        return active_wms_layers

    else:
        for key, layer in layer_list.iteritems():
            if layer.type() == QgsMapLayer.RasterLayer:
                active_wms_layers.append(layer)

        return active_wms_layers


def open_wms_as_raster(iface, wms_url_with_parameters, layer_name):
    """
    Connect to a given wms-server and create a new wms-layer from the url.
    :param iface:
    :type iface:
    :param wms_url_with_parameters: The url to the raster-layer in the form '{parameter=value&}*{url=http://url_to.wms/}'
    :type wms_url_with_parameters: str
    :param layer_name: Name of the new wms raster-layer
    :type layer_name: str
    :return:
    :rtype:
    """
    if iface is not None and wms_url_with_parameters and layer_name and not wms_url_with_parameters.isspace() and not layer_name.isspace():

        rlayer = QgsRasterLayer(wms_url_with_parameters, layer_name, 'wms')

        if not rlayer.isValid():
            return None
        else:
            return rlayer


def zoom_to_layer(iface, layer_name):
    if layer_name and not layer_name.isspace():

        zoom_layer = find_layer_by_name(layer_name)

        # if the shapefile was found set the layer active
        if zoom_layer is not None:
            iface.setActiveLayer(zoom_layer)
            iface.actionZoomToLayer().trigger()


def biuniquify_layer_name(layer_name):
    biunique_name = ''
    if layer_name and not layer_name.isspace():

        biunique_name = layer_name
        suffix = 0

        while(find_layer_by_name(biunique_name) is not None):
            biunique_name = layer_name + str(suffix)
            suffix += 1

    return biunique_name


def change_crs_of_layers(layer_list, dest_crs):
    for layer_name in layer_list:
        layer = find_layer_by_name(layer_name)

        if layer and layer.isValid():
            layer.setCrs(dest_crs)


def move_layer_to_position(iface, layer_name, position):
    """
    Move the layer with the name 'layer_name' to the given position in the iface's Table of Layers
    :param iface: Qgis Interface
    :type iface: QgisInterface
    :param layer_name: Name of the layer
    :type layer_name: str
    :param position: Postion from 0 to max (if position is larger than the number of layers, the layer is always added to the bottom)
    :type position: int
    :return:
    :rtype:
    """
    root = QgsProject.instance().layerTreeRoot()
    layers = root.children()
    for layer_node in layers:
        if layer_node.layerName() == layer_name:
            clone = layer_node.clone()
            root.insertChildNode(position,clone)
            root.removeChildNode(layer_node)
            iface.setActiveLayer(clone.layer())
            break