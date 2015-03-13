# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenEQuarterMain
                                 A QGIS plugin
 The plugin automates the setup for investigating an area.
                              -------------------
        begin                : 2014-10-07
        copyright            : (C) 2014 by Kim Gülle / UdK-Berlin
        email                : kimonline@posteo.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtGui import *
from PyQt4.QtCore import SIGNAL, Qt, QSettings
from qgis.gui import QgsMapToolEmitPoint
from qgis.core import *
from qgis.utils import iface
from socket import gaierror

import sys
import httplib
import unittest
import time
import numpy
import os

from model.progress_model import ProgressModel
from view.oeq_dialogs import Modular_dialog, ProjectSettings_form, ProjectDoesNotExist_dialog, ColorPicker_dialog, MainProcess_dock, RequestWmsUrl_dialog
from view.oeq_ui_classes import QProcessButton
from qgisinteraction import plugin_interaction
from qgisinteraction.plugin_interaction import PstInteraction, OlInteraction
from qgisinteraction import layer_interaction
from qgisinteraction import raster_layer_interaction
from ExportWMSasTif import ExportWMSasTif
from tests import layer_interaction_test


class OpenEQuarterMain:
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        ### Plugin specific settings
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        ### UI specific settings
        # Create the dialogues (after translation) and keep references
        self.main_process_dock = MainProcess_dock()
        self.oeq_project_settings_form = ProjectSettings_form()
        self.color_picker_dlg = ColorPicker_dialog()
        self.project_does_not_exist_dlg = ProjectDoesNotExist_dialog()
        self.request_wms_url_dlg = RequestWmsUrl_dialog()
        self.coordinate_tracker = QgsMapToolEmitPoint(self.iface.mapCanvas())
        self.wms_url = 'crs=EPSG:3068&dpiMode=7&format=image/png&layers=0&styles=&url=http://fbinter.stadt-berlin.de/fb/wms/senstadt/k5'
        self.confirm_selection_of_investigation_area_dlg = Modular_dialog()


        ### Project specific settings
        # the project path is './' as long as the project has not been saved
        self.project_path = QgsProject.instance().readPath('')
        self.project_crs = 'EPSG:3857'
        self.oeq_project = ''


        ### Information needed to use external plugins
        # PointSamplingTool
        self.pst_plugin_name = 'pointsamplingtool'
        self.pst_input_layer_name = 'testpunkte'
        self.pst_output_layer_path = '/Users/VPTtutor/Documents/QGIS/plugin_oeq-qgs_project/Testpunkte/'
        self.pst_output_layer_name = 'pst_out'


        # OpenStreetMap plugin
        self.ol_plugin_name = 'openlayers_plugin'
        # id=0 - Google Physical
        # id=1 - Google Streets
        # id=4 - OpenStreetMap
        self.open_layer_type_id = 4


        ### Default values
        # default extent, after the OSM-layer was loaded (currently: extent of Berlin - Germany)
        self.default_extent = QgsRectangle(numpy.float64(1541791.863584674), numpy.float64(6929650.281509268),
                                           numpy.float64(1434669.8536058515), numpy.float64(6847465.188708487))
        self.default_extent_crs = 'EPSG:3857'
        self.default_scale = 4607478

        # name of the shapefile which will be created to define the investigation area
        self.investigation_shape_layer_name = 'Investigation Area'
        self.investigation_shape_layer_style = os.path.join(self.plugin_dir, 'styles', 'oeq_ia_style.qml')
        self.housing_layer_name = ''
        self.housing_coordinate_layer_name = ''
        # name of the wms-raster which will be loaded and is the basis for the clipping
        self.clipping_raster_layer_name = 'Investigation Area - raster'

        ### Monitor the users progress
        self.progress_model = ProgressModel()

    def initGui(self):
        # Create action that will start plugin configuration
        plugin_icon = QIcon(os.path.join(':/Plugin/icons/OeQ_plugin_icon.png'))
        self.main_action = QAction(plugin_icon, u"OpenEQuarter-Process", self.iface.mainWindow())
        # connect the action to the run method
        self.main_action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.main_action)
        self.iface.addPluginToMenu(u"&OpenEQuarter", self.main_action)

        clipping_icon = QIcon(os.path.join(':','Plugin', 'icons', 'scissor.png'))
        self.clipping_action = QAction(clipping_icon, u"Extract extent from active WMS", self.iface.mainWindow())
        self.clipping_action.triggered.connect(lambda: self.clip_from_raster(self.iface.activeLayer()))
        self.iface.addToolBarIcon(self.clipping_action)
        self.iface.addPluginToMenu(u"&OpenEQuarter", self.clipping_action)

        testing_icon = QIcon(os.path.join(':','Plugin', 'icons', 'lightbulb.png'))
        self.testing_action = QAction(testing_icon, u"Run all unit-tests", self.iface.mainWindow())
        self.testing_action.triggered.connect(lambda: self.run_tests())
        self.iface.addToolBarIcon(self.testing_action)
        self.iface.addPluginToMenu(u"&OpenEQuarter", self.testing_action)

        self.main_process_dock.process_button_next.clicked.connect(self.continue_process)
        self.main_process_dock.process_button_auto.clicked.connect(self.auto_run)

        for page in self.main_process_dock.selection_to_page.values():
            for button in page.children():
                if isinstance(button, QProcessButton):
                    self.main_process_dock.connect(button, SIGNAL('process_button_click'), self.process_button_clicked)

        settings_dropdown_menu = QMenu()
        settings_dropdown_menu.addAction('Open project setup..', self.open_settings)
        settings_dropdown_menu.addAction('Save current progress', self.save_progress)
        settings_dropdown_menu.addAction('Save current progress as..', self.save_progress_as)
        settings_dropdown_menu.addAction('Open OeQ-Project..', self.open_progress)

        tools_dropdown_menu = QMenu()
        tools_dropdown_menu.addAction('Color Picker', self.chose_color)
        tools_dropdown_menu.addAction('Load layer from WMS', self.load_wms)

        self.main_process_dock.tools_dropdown_btn.setMenu(tools_dropdown_menu)
        self.main_process_dock.settings_dropdown_btn.setMenu(settings_dropdown_menu)

        self.main_process_dock.connect(QgsMapLayerRegistry.instance(), SIGNAL('legendLayersAdded(QList< QgsMapLayer * >)'), self.update_layer_positions)

    def update_layer_positions(self):
        layer_interaction.move_layer_to_position(self.iface, self.investigation_shape_layer_name, 0)
        layer_interaction.move_layer_to_position(self.iface, self.housing_coordinate_layer_name, 1)
        layer_interaction.move_layer_to_position(self.iface, self.housing_layer_name, 2)

    def open_settings(self):
        self.oeq_project_settings_form.show()

    def open_progress(self):
        print 'Open Project'

    def save_progress(self):
        print 'Save progress'

    def save_progress_as(self):
        print 'Save as'

    def load_wms(self):
        print('Load wms')

    def chose_color(self):
        self.coordinate_tracker.canvasClicked.connect(self.handle_canvas_click)
        self.iface.mapCanvas().setMapTool(self.coordinate_tracker)
        self.color_picker_dlg.refresh_layers_dropdown.clicked.connect(self.refresh_layer_list)
        self.refresh_layer_list()

        dropdown = self.color_picker_dlg.layers_dropdown
        dropdown.currentIndexChanged.connect(self.color_picker_dlg.update_color_values)
        dropdown.currentIndexChanged.connect(lambda: layer_interaction.move_layer_to_position(self.iface, dropdown.currentText(), 0))
        self.color_picker_dlg.show()
        save_or_abort = self.color_picker_dlg.exec_()

        if save_or_abort:
            layer = self.iface.activeLayer()
            out_path = os.path.dirname(layer.publicSource())
            out_path = os.path.join(out_path, layer.name() + '.txt')
            self.color_picker_dlg.update_color_values()
            self.color_picker_dlg.color_entry_manager.write_map_to_disk(layer.name(), out_path)
        else:
            self.color_picker_dlg.__init__()

        self.iface.actionPan().trigger()

    # ToDo Check if this has to be put in a separate method
    def refresh_layer_list(self):
        dropdown = self.color_picker_dlg.layers_dropdown
        dropdown.clear()
        wms_list = layer_interaction.get_wms_layer_list(self.iface, visibility='visible')

        layer = None
        for layer in wms_list:
            source = layer.publicSource()
            if os.path.basename(source).endswith('.tif'):
                dropdown.addItem(layer.name())
                self.color_picker_dlg.color_entry_manager.add_layer(layer.name())

        layer_interaction.move_layer_to_position(self.iface, layer, 0)

    def handle_canvas_click(self, point, button):
        canvas = self.iface.mapCanvas()
        crs = canvas.mapRenderer().destinationCrs()
        raster = self.iface.activeLayer()

        if raster is not None:
            color = raster_layer_interaction.extract_color_at_point(raster, point, crs)

            if isinstance(color, QColor):
                self.color_picker_dlg.add_color(color)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&OpenEQuarter", self.main_action)
        self.iface.removePluginMenu(u"&OpenEQuarter", self.clipping_action)
        self.iface.removePluginMenu(u"&OpenEQuarter", self.testing_action)
        self.iface.removeToolBarIcon(self.main_action)
        self.iface.removeToolBarIcon(self.clipping_action)
        self.iface.removeToolBarIcon(self.testing_action)
        self.main_process_dock.disconnect(QgsMapLayerRegistry.instance(), SIGNAL('legendLayersAdded(QList< QgsMapLayer * >)'), self.update_layer_positions)

    def create_project_ifNotExists(self):
        """
        If the current workspace has not been saved as a project, prompt the user to "Save As..." project
        :return:
        :rtype:
        """
        # read the current project path
        self.project_path = QgsProject.instance().readPath('./')

        # if the path is './', the project has not yet been saved
        if self.project_path == './':

            # prompt the user to save the project
            self.project_does_not_exist_dlg.show()
            yes_to_save = self.project_does_not_exist_dlg.exec_()

            if yes_to_save:
                # trigger qgis "Save As"-function
                iface.actionSaveProjectAs().trigger()

    def osm_layer_is_loaded(self):
        """
        Iterate over all layers and check if an osm plugin-layer exists.
        :return True if the layer is available:
        :rtype bool:
        """
        for layer in QgsMapLayerRegistry.instance().mapLayers():
            if 'OpenLayers_plugin_layer' in layer:
                return True

        return False

    def zoom_to_default_extent(self):
        """
        Set the canvas-extent to the extent and scale specified in self.default_extent and self.default_scale
        :return:
        :rtype:
        """

        print "zoom"
        canvas = self.iface.mapCanvas()
        layers = QgsMapLayerRegistry.instance().mapLayers()

        if len(layers) >= 0 and len(layers) <= 2:
            print "zoom2"
            canvas.zoomScale(self.default_scale)
            canvas.setExtent(self.default_extent)
            canvas.refresh()

    def confirm_selection_of_investigation_area(self, layer_name):
        """
        Select the layer named 'layer_name' from layers list and trigger the ToggleEditing button
        :param layer_name: Name of the layer whose editing mode shall be triggered
        :type layer_name: str
        :return:
        :rtype:
        """
        if layer_name and not layer_name.isspace():

            edit_layer = layer_interaction.find_layer_by_name(layer_name)

            # if the layer was found, prompt the user to confirm the adding-feature-process was finished
            if edit_layer:

                self.confirm_selection_of_investigation_area_dlg.show()
                confirmation = self.confirm_selection_of_investigation_area_dlg.exec_()

                # if the finalization of the process was confirmed, return True
                if confirmation:
                    return True

                else:
                    return False

    # method currently not in use
    def request_wms_layer_url(self):
        """
        Open a dialog and request an url to a wms-server. Check if the given url is valid, by trying to connect to the server.
        :return:
        :rtype:
        """
        self.request_wms_url_dlg.show()
        url_confirmed = self.request_wms_url_dlg.exec_()

        # if 'ok' was hit, get the url
        if url_confirmed:
            wms_url = self.request_wms_url_dlg.wms_url.text()

            try:
                if wms_url.startswith("http"):
                    socket = httplib.HTTPConnection(wms_url[7:])
                    socket.connect()
                else:
                    socket = httplib.HTTPConnection(wms_url)
                    socket.connect()

            except (httplib.HTTPException, gaierror) as ex:
                print "Invalid url"
                return

            self.wms_url = wms_url

    def set_project_crs(self, crs):
        """
        Set the project crs to the given crs and do a re-projection to keep the currently viewed extent focused
        :param crs: The new crs to set the project to
        :type crs: str
        :return:
        :rtype:
        """
        # if the given crs is valid
        if not crs.isspace() and QgsCoordinateReferenceSystem(crs):

            canvas = self.iface.mapCanvas()

            extent = canvas.extent()  # save formerly viewed extent
            current_crs = self.get_project_crs()  # get project-crs
            current_scale = canvas.scale()

            renderer = canvas.mapRenderer()
            new_crs = QgsCoordinateReferenceSystem(crs)
            renderer.setDestinationCrs(new_crs)

            canvas.zoomScale(current_scale)

            if not current_crs == new_crs:
                # set extent, by transforming the formerly saved extent to new Projection
                coord_transformer = QgsCoordinateTransform(current_crs, new_crs)
                extent = coord_transformer.transform(extent)

            canvas.setExtent(extent)
            canvas.refresh()

    def get_project_crs(self):
        """
        Return the project crs
        :return: The project crs
        :rtype: QgsCoordinateReferenceSystem
        """

        canvas = iface.mapCanvas()
        crs = canvas.mapSettings().destinationCrs()

        return crs

    def clip_from_raster(self, raster_layer):

        try:
            # set the rasterlayer as active, since only the active layer will be clipped and start the export
            self.iface.setActiveLayer(raster_layer)
            pyramid_exporter = ExportWMSasTif(self.iface)
            return pyramid_exporter.export(raster_layer.name())

        except None as exception:
            print exception
            return None

    def clip_zoom_to_layer_view_from_raster(self, layer_name):
        """
        Zoom to a given vector-layer, containing shape files. Extract the currently viewed extent from an underlying raster-layer into a new .tif and open it.
        :param layer_name: Name of the vector-layer
        :type layer_name: str
        :return:
        :rtype:
        """
        try:
            investigation_shape = layer_interaction.find_layer_by_name(layer_name)

            # an investigation shape is needed, to trigger the zoom to layer function
            if investigation_shape is not None and investigation_shape.featureCount() > 0:

                # zoom
                self.iface.setActiveLayer(investigation_shape)
                self.iface.actionZoomToLayer().trigger()

                # clip extent from visible raster layers
                # save visible layers and set them invisible afterwards, to prevent further from the wms-server
                raster_layers = layer_interaction.get_wms_layer_list(self.iface, 'visible')
                for layer in raster_layers:
                    self.iface.legendInterface().setLayerVisible(layer, False)

                clipped_layers = []
                for clipping_raster in raster_layers:
                    clipped_layers.append(self.clip_from_raster(clipping_raster))

                return clipped_layers
        except None as exception:
            print exception
            return None

    def load_housing_layer(self):
        # ToDo
        return

    def add_housing_coordinates(self):
        # ToDo
        return

    # step 0.0
    def handle_ol_plugin_installed(self):
        return plugin_interaction.get_plugin_ifexists(self.ol_plugin_name) is not None

    # step 0.1
    def handle_pst_plugin_installed(self):
        return plugin_interaction.get_plugin_ifexists(self.pst_plugin_name) is not None

    # step 0.2
    def handle_project_created(self):
        # if no project exists, create one first
        self.create_project_ifNotExists()
        self.project_path = QgsProject.instance().readPath('./')

        # if project was created stop execution
        if self.project_path != './':
            return True
        else:
            return False

    # step 0.3
    def handle_osm_layer_loaded(self):
        if self.osm_layer_is_loaded():
            return True

        else:
            ol_plugin = OlInteraction(self.ol_plugin_name)
        # self.enable_on_the_fly_projection()
        # self.set_project_crs(self.default_extent_crs)

            if ol_plugin.open_osm_layer(self.open_layer_type_id):
                self.zoom_to_default_extent()
                return True

            else:
                return False

    # step 1.0
    def handle_temp_shapefile_created(self):
        investigation_area = layer_interaction.create_temporary_layer(self.investigation_shape_layer_name, 'Polygon',
                                                                     self.project_crs)

        if investigation_area is not None:
            layer_interaction.add_style_to_layer(self.investigation_shape_layer_style, investigation_area)
            layer_interaction.add_layer_to_registry(investigation_area)
            return True
        else:
            return False

    # step 1.1
    def handle_editing_temp_shapefile_started(self):
        layer_interaction.trigger_edit_mode(self.iface, self.investigation_shape_layer_name)
        return True

    # step 1.2
    def handle_investigation_area_selected(self):
        self.confirm_selection_of_investigation_area_dlg.set_dialog_text(
            "Click 'OK' once the investigatoion area is selected.", "Define investigaion area")
        ia_covered = self.confirm_selection_of_investigation_area(self.investigation_shape_layer_name)
        return ia_covered

    # step 1.3
    def handle_editing_temp_shapefile_stopped(self):
        layer_interaction.trigger_edit_mode(self.iface, self.investigation_shape_layer_name, 'off')
        try:
            investigation_area = layer_interaction.find_layer_by_name(self.investigation_shape_layer_name)
            disk_layer = layer_interaction.write_vector_layer_to_disk(investigation_area, os.path.join(self.project_path, investigation_area.name()))

            if disk_layer.isValid():
                layer_interaction.hide_or_remove_layer(self.investigation_shape_layer_name, 'remove')
                layer_interaction.add_layer_to_registry(disk_layer)
                layer_interaction.add_style_to_layer(self.investigation_shape_layer_style, disk_layer)
                # trigger the edit-mode, to have the style displayed.
                layer_interaction.trigger_edit_mode(self.iface, disk_layer.name())
                layer_interaction.trigger_edit_mode(self.iface, disk_layer.name(), 'off')
                disk_layer.setLayerName(self.investigation_shape_layer_name)

        except IOError, Error:
            print('The "Investigation Area"-layer could not be saved to disk:')
            print(Error)
        return True

    # step 2.0
    def handle_raster_loaded(self):
        # self.request_wms_layer_url()
        investigation_raster_layer = layer_interaction.open_wms_as_raster(self.iface, self.wms_url, self.clipping_raster_layer_name)

        if investigation_raster_layer is not None and investigation_raster_layer.isValid():
            layer_interaction.add_layer_to_registry(investigation_raster_layer)
            self.iface.setActiveLayer(investigation_raster_layer)
            return True
        else:
            self.iface.actionAddWmsLayer().trigger()
            return True

    # step 2.1
    def handle_extent_clipped(self):
        extracted_layers = self.clip_zoom_to_layer_view_from_raster(self.investigation_shape_layer_name)
        layer_interaction.hide_or_remove_layer('OpenStreetMap', 'hide', self.iface)

        for layer_name in extracted_layers:
            try:
                layer = layer_interaction.find_layer_by_name(layer_name)
                raster_layer_interaction.gdal_warp_layer(layer, self.project_crs)
                path_geo = layer.publicSource()
                path_transformed = path_geo.replace('_geo.tif', '_transformed.tif')

                if os.path.exists(path_transformed):
                    # change validation to surpress missing-crs prompt
                    old_validation = str(QSettings().value('/Projections/defaultBehaviour', 'useProject'))
                    QSettings().setValue('/Projections/defaultBehaviour', 'useProject')

                    layer_interaction.hide_or_remove_layer(layer_name,'remove',self.iface)

                    rlayer = QgsRasterLayer(path_transformed, layer_name)
                    rlayer.setCrs(QgsCoordinateReferenceSystem(self.project_crs))
                    QgsMapLayerRegistry.instance().addMapLayer(rlayer)
                    os.remove(path_geo)
                    self.iface.mapCanvas().refresh()
                    # restore former settings
                    QSettings().setValue('/Projections/defaultBehaviour', old_validation)
            except (OSError, AttributeError) as Clipping_Error:
                print(Clipping_Error)
                pass

        time.sleep(1.0)
        return True

    # step 2.2
    def handle_pyramids_built(self):
        return True

    # step 3.0
    def handle_temp_pointlayer_created(self):
        pst_input_layer = layer_interaction.create_temporary_layer(self.pst_input_layer_name, 'Point',
                                                                  self.project_crs)
        layer_interaction.add_layer_to_registry(pst_input_layer)
        return True

    # step 3.1
    def handle_editing_temp_pointlayer_started(self):
        layer_interaction.trigger_edit_mode(self.iface, self.pst_input_layer_name)
        return True

    # step 3.2
    def handle_points_of_interest_defined(self):
        self.confirm_selection_of_investigation_area_dlg.set_dialog_text(
            "Click 'OK' once the sampling points are selected.", "Choose sample points")
        points_selected = self.confirm_selection_of_investigation_area(self.pst_input_layer_name)
        return points_selected

    # step 3.3
    def handle_editing_temp_pointlayer_stopped(self):
        layer_interaction.trigger_edit_mode(self.iface, self.pst_input_layer_name, 'off')
        return True

    # step 3.4
    def handle_information_sampled(self):
        pst_plugin = plugin_interaction.get_plugin_ifexists(self.pst_plugin_name)
        psti = PstInteraction(pst_plugin, iface)

        psti.set_input_layer(self.pst_input_layer_name)
        psti.select_files_for_sampling()

        pst_output_layer = psti.start_sampling(self.project_path, self.pst_output_layer_name)
        vlayer = QgsVectorLayer(pst_output_layer, layer_interaction.biuniquify_layer_name('pst_out'), "ogr")
        layer_interaction.add_layer_to_registry(vlayer)
        return True

    def continue_process(self):
        """
        Call the appropriate handle-function, depending on the progress-step, that shall has to be executed next.
        :return:
        :rtype:
        """
        try:
            next_open_step_no = self.progress_model.last_step_executed + 1
            next_open_step = self.progress_model.get_step_list()[next_open_step_no]

            step_page = self.main_process_dock.findChild(QProcessButton, next_open_step + '_chckBox').parent()
            step_section = step_page.objectName()[0:-5]

            if self.progress_model.prerequisites_are_given(next_open_step):
                handler = 'handle_' + next_open_step
                next_call = getattr(self, handler)

                step_completed = next_call()
                self.progress_model.update_progress(step_section, next_open_step, step_completed)
                self.main_process_dock.set_checkbox_on_page(next_open_step + '_chckBox', step_section + '_page', step_completed)

                if self.progress_model.is_section_done(step_section):
                    self.main_process_dock.set_current_page_done(True)
        except IndexError, error:
            print error

    def process_button_clicked(self, *args):
        """
        Call the appropriate handle-function, depending on the objet which triggered the function call.
        :param args: The sender name and the sender object in a list
        :type args: list
        :return:
        :rtype:
        """
        sender_name = args[0]
        sender_object = args[1]
        next_step = sender_name[:-8]

        next_page = sender_object.parent()
        next_section = next_page.objectName()[0:-5]

        # for debugging uncomment the following line
        if True:
        #if self.progress_model.prerequisites_are_given(next_step) or True:
            handler = 'handle_' + next_step
            next_call = getattr(self, handler)

            is_done = next_call()
            self.progress_model.update_progress(next_section, next_step, is_done)
            self.main_process_dock.go_to_page(next_page.accessibleName())
            self.main_process_dock.set_checkbox_on_page(next_step + '_chckBox', next_section + '_page', is_done)

    def run(self):
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.main_process_dock)

        if self.oeq_project == '':
            self.oeq_project_settings_form.show()
            save_or_abort = self.oeq_project_settings_form.exec_()

        print save_or_abort
        if save_or_abort:
            self.check_status()

    def run_tests(self):
        test_class = layer_interaction_test.LayerInteraction_test
        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(test_class)

        suite = unittest.TestSuite()
        for test_method in test_names:
            suite.addTest(test_class(test_method, self.iface))

        unittest.TextTestRunner(sys.stdout).run(suite)

    def check_status(self):

        self.continue_process() #OL-Plugin
        self.continue_process() #PST-Plugin
        self.continue_process() #Proje. saved

        investigation_layer = layer_interaction.find_layer_by_name(self.investigation_shape_layer_name)

        if self.osm_layer_is_loaded() or investigation_layer:
            self.set_next_step_done(True) # open OL-map

            if investigation_layer:
                self.set_next_step_done(True) # create shapefile

                if investigation_layer.featureCount() > 0:
                    self.set_next_step_done(True) # activate edit mode
                    self.set_next_step_done(True) # confirm selection
                    self.set_next_step_done(True) # deactivate edit mode

    def set_next_step_done(self, is_done):
        try:
            next_open_step_no = self.progress_model.last_step_executed + 1
            next_open_step = self.progress_model.get_step_list()[next_open_step_no]

            step_page = self.main_process_dock.findChild(QProcessButton, next_open_step + '_chckBox').parent()
            step_section = step_page.objectName()[0:-5]

            self.progress_model.update_progress(step_section, next_open_step, is_done)
            self.main_process_dock.set_checkbox_on_page(next_open_step + '_chckBox', step_section + '_page', is_done)

            if self.progress_model.is_section_done(step_section):
                self.main_process_dock.set_current_page_done(is_done)

        except IndexError, error:
                print error

    def auto_run(self):
        steps = self.progress_model.get_step_list()
        next = self.progress_model.last_step_executed

        try:
            for i in range(len(steps)):
                if self.iface.mapCanvas().isDrawing():
                    i - 1
                else:
                    next = self.progress_model.last_step_executed + 1
                    time.sleep(1.5)
                    self.continue_process()
                    i = next

        except IndexError, error:
            print error



