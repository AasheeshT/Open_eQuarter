# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainstay_process_dialog.ui'
#
# Created: Thu Dec  4 13:12:40 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainstayProcess_dialog(object):
    def setupUi(self, MainstayProcess_dialog):
        MainstayProcess_dialog.setObjectName(_fromUtf8("MainstayProcess_dialog"))
        MainstayProcess_dialog.setEnabled(True)
        MainstayProcess_dialog.resize(614, 513)
        MainstayProcess_dialog.setMinimumSize(QtCore.QSize(614, 513))
        MainstayProcess_dialog.setMaximumSize(QtCore.QSize(812, 513))
        MainstayProcess_dialog.setAutoFillBackground(False)
        MainstayProcess_dialog.setStyleSheet(_fromUtf8(""))
        MainstayProcess_dialog.setSizeGripEnabled(False)
        MainstayProcess_dialog.setModal(False)
        self.buttonBox = QtGui.QDialogButtonBox(MainstayProcess_dialog)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QtCore.QRect(260, 405, 211, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.process_page = QtGui.QStackedWidget(MainstayProcess_dialog)
        self.process_page.setEnabled(False)
        self.process_page.setGeometry(QtCore.QRect(160, 10, 440, 391))
        self.process_page.setAutoFillBackground(False)
        self.process_page.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.process_page.setFrameShape(QtGui.QFrame.Panel)
        self.process_page.setFrameShadow(QtGui.QFrame.Sunken)
        self.process_page.setLineWidth(2)
        self.process_page.setMidLineWidth(1)
        self.process_page.setObjectName(_fromUtf8("process_page"))
        self.project_basics_page = QtGui.QWidget()
        self.project_basics_page.setObjectName(_fromUtf8("project_basics_page"))
        self.ol_plugin_installed_chckBox = QtGui.QCheckBox(self.project_basics_page)
        self.ol_plugin_installed_chckBox.setEnabled(False)
        self.ol_plugin_installed_chckBox.setGeometry(QtCore.QRect(10, 15, 261, 41))
        self.ol_plugin_installed_chckBox.setCheckable(True)
        self.ol_plugin_installed_chckBox.setTristate(True)
        self.ol_plugin_installed_chckBox.setObjectName(_fromUtf8("ol_plugin_installed_chckBox"))
        self.project_created_chckBox = QtGui.QCheckBox(self.project_basics_page)
        self.project_created_chckBox.setEnabled(False)
        self.project_created_chckBox.setGeometry(QtCore.QRect(10, 95, 261, 41))
        self.project_created_chckBox.setStyleSheet(_fromUtf8(""))
        self.project_created_chckBox.setCheckable(True)
        self.project_created_chckBox.setObjectName(_fromUtf8("project_created_chckBox"))
        self.osm_layer_loaded_chckBox = QtGui.QCheckBox(self.project_basics_page)
        self.osm_layer_loaded_chckBox.setEnabled(False)
        self.osm_layer_loaded_chckBox.setGeometry(QtCore.QRect(10, 135, 261, 41))
        self.osm_layer_loaded_chckBox.setCheckable(True)
        self.osm_layer_loaded_chckBox.setObjectName(_fromUtf8("osm_layer_loaded_chckBox"))
        self.pst_plugin_installed_chckBox = QtGui.QCheckBox(self.project_basics_page)
        self.pst_plugin_installed_chckBox.setEnabled(False)
        self.pst_plugin_installed_chckBox.setGeometry(QtCore.QRect(10, 55, 261, 41))
        self.pst_plugin_installed_chckBox.setCheckable(True)
        self.pst_plugin_installed_chckBox.setObjectName(_fromUtf8("pst_plugin_installed_chckBox"))
        self.process_page.addWidget(self.project_basics_page)
        self.investigation_area_page = QtGui.QWidget()
        self.investigation_area_page.setObjectName(_fromUtf8("investigation_area_page"))
        self.temp_shapefile_created_chckBox = QtGui.QCheckBox(self.investigation_area_page)
        self.temp_shapefile_created_chckBox.setEnabled(False)
        self.temp_shapefile_created_chckBox.setGeometry(QtCore.QRect(10, 15, 261, 41))
        self.temp_shapefile_created_chckBox.setCheckable(True)
        self.temp_shapefile_created_chckBox.setObjectName(_fromUtf8("temp_shapefile_created_chckBox"))
        self.editing_temp_shapefile_started_chckBox = QtGui.QCheckBox(self.investigation_area_page)
        self.editing_temp_shapefile_started_chckBox.setEnabled(False)
        self.editing_temp_shapefile_started_chckBox.setGeometry(QtCore.QRect(10, 55, 261, 41))
        self.editing_temp_shapefile_started_chckBox.setCheckable(True)
        self.editing_temp_shapefile_started_chckBox.setObjectName(_fromUtf8("editing_temp_shapefile_started_chckBox"))
        self.investigation_area_selected_chckBox = QtGui.QCheckBox(self.investigation_area_page)
        self.investigation_area_selected_chckBox.setEnabled(False)
        self.investigation_area_selected_chckBox.setGeometry(QtCore.QRect(10, 95, 411, 41))
        self.investigation_area_selected_chckBox.setCheckable(True)
        self.investigation_area_selected_chckBox.setObjectName(_fromUtf8("investigation_area_selected_chckBox"))
        self.editing_temp_shapefile_stopped_chckBox = QtGui.QCheckBox(self.investigation_area_page)
        self.editing_temp_shapefile_stopped_chckBox.setEnabled(False)
        self.editing_temp_shapefile_stopped_chckBox.setGeometry(QtCore.QRect(10, 135, 261, 41))
        self.editing_temp_shapefile_stopped_chckBox.setCheckable(True)
        self.editing_temp_shapefile_stopped_chckBox.setObjectName(_fromUtf8("editing_temp_shapefile_stopped_chckBox"))
        self.process_page.addWidget(self.investigation_area_page)
        self.building_shapes_page = QtGui.QWidget()
        self.building_shapes_page.setObjectName(_fromUtf8("building_shapes_page"))
        self.raster_loaded_chckBox = QtGui.QCheckBox(self.building_shapes_page)
        self.raster_loaded_chckBox.setEnabled(False)
        self.raster_loaded_chckBox.setGeometry(QtCore.QRect(10, 15, 261, 41))
        self.raster_loaded_chckBox.setCheckable(True)
        self.raster_loaded_chckBox.setObjectName(_fromUtf8("raster_loaded_chckBox"))
        self.extent_clipped_chckBox = QtGui.QCheckBox(self.building_shapes_page)
        self.extent_clipped_chckBox.setEnabled(False)
        self.extent_clipped_chckBox.setGeometry(QtCore.QRect(10, 55, 321, 41))
        self.extent_clipped_chckBox.setCheckable(True)
        self.extent_clipped_chckBox.setObjectName(_fromUtf8("extent_clipped_chckBox"))
        self.pyramids_built_chckBox = QtGui.QCheckBox(self.building_shapes_page)
        self.pyramids_built_chckBox.setEnabled(False)
        self.pyramids_built_chckBox.setGeometry(QtCore.QRect(10, 95, 321, 41))
        self.pyramids_built_chckBox.setCheckable(True)
        self.pyramids_built_chckBox.setObjectName(_fromUtf8("pyramids_built_chckBox"))
        self.process_page.addWidget(self.building_shapes_page)
        self.sampling_points_page = QtGui.QWidget()
        self.sampling_points_page.setObjectName(_fromUtf8("sampling_points_page"))
        self.temp_pointlayer_created_chckBox = QtGui.QCheckBox(self.sampling_points_page)
        self.temp_pointlayer_created_chckBox.setEnabled(False)
        self.temp_pointlayer_created_chckBox.setGeometry(QtCore.QRect(10, 15, 261, 41))
        self.temp_pointlayer_created_chckBox.setCheckable(True)
        self.temp_pointlayer_created_chckBox.setObjectName(_fromUtf8("temp_pointlayer_created_chckBox"))
        self.editing_temp_pointlayer_started_chckBox = QtGui.QCheckBox(self.sampling_points_page)
        self.editing_temp_pointlayer_started_chckBox.setEnabled(False)
        self.editing_temp_pointlayer_started_chckBox.setGeometry(QtCore.QRect(10, 55, 261, 41))
        self.editing_temp_pointlayer_started_chckBox.setCheckable(True)
        self.editing_temp_pointlayer_started_chckBox.setObjectName(_fromUtf8("editing_temp_pointlayer_started_chckBox"))
        self.points_of_interest_defined_chckBox = QtGui.QCheckBox(self.sampling_points_page)
        self.points_of_interest_defined_chckBox.setEnabled(False)
        self.points_of_interest_defined_chckBox.setGeometry(QtCore.QRect(10, 95, 411, 41))
        self.points_of_interest_defined_chckBox.setCheckable(True)
        self.points_of_interest_defined_chckBox.setObjectName(_fromUtf8("points_of_interest_defined_chckBox"))
        self.editing_temp_pointlayer_stopped_chckBox = QtGui.QCheckBox(self.sampling_points_page)
        self.editing_temp_pointlayer_stopped_chckBox.setEnabled(False)
        self.editing_temp_pointlayer_stopped_chckBox.setGeometry(QtCore.QRect(10, 135, 261, 41))
        self.editing_temp_pointlayer_stopped_chckBox.setCheckable(True)
        self.editing_temp_pointlayer_stopped_chckBox.setObjectName(_fromUtf8("editing_temp_pointlayer_stopped_chckBox"))
        self.information_sampled_chckBox = QtGui.QCheckBox(self.sampling_points_page)
        self.information_sampled_chckBox.setEnabled(False)
        self.information_sampled_chckBox.setGeometry(QtCore.QRect(10, 175, 381, 41))
        self.information_sampled_chckBox.setCheckable(True)
        self.information_sampled_chckBox.setObjectName(_fromUtf8("information_sampled_chckBox"))
        self.process_page.addWidget(self.sampling_points_page)
        self.project_basics_btn = QtGui.QToolButton(MainstayProcess_dialog)
        self.project_basics_btn.setEnabled(True)
        self.project_basics_btn.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.project_basics_btn.setStyleSheet(_fromUtf8(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:0.5, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(230, 230, 230, 203));\n"
"    border: 1px solid rgb(192,192,192);\n"
"}\n"
":checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.495074, y2:0.284, stop:0 rgba(204, 204, 204, 255), stop:1 rgba(239, 239, 239, 255));\n"
"    border: 1px solid rgb(192,192,192);\n"
"}"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/openmark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/checkmark.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.project_basics_btn.setIcon(icon)
        self.project_basics_btn.setIconSize(QtCore.QSize(20, 20))
        self.project_basics_btn.setCheckable(True)
        self.project_basics_btn.setChecked(False)
        self.project_basics_btn.setAutoRepeat(False)
        self.project_basics_btn.setAutoExclusive(False)
        self.project_basics_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.project_basics_btn.setAutoRaise(False)
        self.project_basics_btn.setArrowType(QtCore.Qt.NoArrow)
        self.project_basics_btn.setObjectName(_fromUtf8("project_basics_btn"))
        self.investigation_area_btn = QtGui.QToolButton(MainstayProcess_dialog)
        self.investigation_area_btn.setEnabled(True)
        self.investigation_area_btn.setGeometry(QtCore.QRect(10, 40, 141, 31))
        self.investigation_area_btn.setStyleSheet(_fromUtf8(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:0.5, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(230, 230, 230, 203));\n"
"    border: 1px solid rgb(192,192,192);\n"
"}\n"
":checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.495074, y2:0.284, stop:0 rgba(204, 204, 204, 255), stop:1 rgba(239, 239, 239, 255));\n"
"    border: 1px solid rgb(192,192,192);\n"
"}"))
        self.investigation_area_btn.setIcon(icon)
        self.investigation_area_btn.setIconSize(QtCore.QSize(20, 20))
        self.investigation_area_btn.setCheckable(True)
        self.investigation_area_btn.setChecked(False)
        self.investigation_area_btn.setAutoRepeat(False)
        self.investigation_area_btn.setAutoExclusive(False)
        self.investigation_area_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.investigation_area_btn.setAutoRaise(False)
        self.investigation_area_btn.setArrowType(QtCore.Qt.NoArrow)
        self.investigation_area_btn.setObjectName(_fromUtf8("investigation_area_btn"))
        self.building_shapes_btn = QtGui.QToolButton(MainstayProcess_dialog)
        self.building_shapes_btn.setEnabled(True)
        self.building_shapes_btn.setGeometry(QtCore.QRect(10, 90, 141, 31))
        self.building_shapes_btn.setStyleSheet(_fromUtf8(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:0.5, stop:0 rgba(175, 175, 175, 255), stop:1 rgba(230, 230, 230, 203));\n"
"    border: 1px solid rgb(192,192,192);\n"
"}\n"
":checked {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.495074, y2:0.284, stop:0 rgba(204, 204, 204, 255), stop:1 rgba(239, 239, 239, 255));\n"
"    border: 1px solid rgb(192,192,192);\n"
"}"))
        self.building_shapes_btn.setIcon(icon)
        self.building_shapes_btn.setIconSize(QtCore.QSize(20, 20))
        self.building_shapes_btn.setCheckable(True)
        self.building_shapes_btn.setChecked(False)
        self.building_shapes_btn.setAutoRepeat(False)
        self.building_shapes_btn.setAutoExclusive(False)
        self.building_shapes_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.building_shapes_btn.setAutoRaise(False)
        self.building_shapes_btn.setArrowType(QtCore.Qt.NoArrow)
        self.building_shapes_btn.setObjectName(_fromUtf8("building_shapes_btn"))
        self.sampling_points_btn = QtGui.QToolButton(MainstayProcess_dialog)
        self.sampling_points_btn.setEnabled(True)
        self.sampling_points_btn.setGeometry(QtCore.QRect(10, 120, 141, 31))
        self.sampling_points_btn.setIcon(icon)
        self.sampling_points_btn.setIconSize(QtCore.QSize(20, 20))
        self.sampling_points_btn.setCheckable(True)
        self.sampling_points_btn.setChecked(False)
        self.sampling_points_btn.setAutoRepeat(False)
        self.sampling_points_btn.setAutoExclusive(False)
        self.sampling_points_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.sampling_points_btn.setAutoRaise(False)
        self.sampling_points_btn.setArrowType(QtCore.Qt.NoArrow)
        self.sampling_points_btn.setObjectName(_fromUtf8("sampling_points_btn"))
        self.oeqstepbutton_5 = QtGui.QToolButton(MainstayProcess_dialog)
        self.oeqstepbutton_5.setEnabled(True)
        self.oeqstepbutton_5.setGeometry(QtCore.QRect(10, 170, 141, 31))
        self.oeqstepbutton_5.setIcon(icon)
        self.oeqstepbutton_5.setIconSize(QtCore.QSize(20, 20))
        self.oeqstepbutton_5.setCheckable(True)
        self.oeqstepbutton_5.setChecked(False)
        self.oeqstepbutton_5.setAutoRepeat(False)
        self.oeqstepbutton_5.setAutoExclusive(False)
        self.oeqstepbutton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.oeqstepbutton_5.setAutoRaise(False)
        self.oeqstepbutton_5.setArrowType(QtCore.Qt.NoArrow)
        self.oeqstepbutton_5.setObjectName(_fromUtf8("oeqstepbutton_5"))
        self.oeqstepbutton_6 = QtGui.QToolButton(MainstayProcess_dialog)
        self.oeqstepbutton_6.setEnabled(True)
        self.oeqstepbutton_6.setGeometry(QtCore.QRect(10, 200, 141, 31))
        self.oeqstepbutton_6.setIcon(icon)
        self.oeqstepbutton_6.setIconSize(QtCore.QSize(20, 20))
        self.oeqstepbutton_6.setCheckable(True)
        self.oeqstepbutton_6.setChecked(False)
        self.oeqstepbutton_6.setAutoRepeat(False)
        self.oeqstepbutton_6.setAutoExclusive(False)
        self.oeqstepbutton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.oeqstepbutton_6.setAutoRaise(False)
        self.oeqstepbutton_6.setArrowType(QtCore.Qt.NoArrow)
        self.oeqstepbutton_6.setObjectName(_fromUtf8("oeqstepbutton_6"))
        self.oeqstepbutton_7 = QtGui.QToolButton(MainstayProcess_dialog)
        self.oeqstepbutton_7.setEnabled(True)
        self.oeqstepbutton_7.setGeometry(QtCore.QRect(10, 230, 141, 31))
        self.oeqstepbutton_7.setIcon(icon)
        self.oeqstepbutton_7.setIconSize(QtCore.QSize(20, 20))
        self.oeqstepbutton_7.setCheckable(True)
        self.oeqstepbutton_7.setChecked(False)
        self.oeqstepbutton_7.setAutoRepeat(False)
        self.oeqstepbutton_7.setAutoExclusive(False)
        self.oeqstepbutton_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.oeqstepbutton_7.setAutoRaise(False)
        self.oeqstepbutton_7.setArrowType(QtCore.Qt.NoArrow)
        self.oeqstepbutton_7.setObjectName(_fromUtf8("oeqstepbutton_7"))
        self.oeqstepbutton_8 = QtGui.QToolButton(MainstayProcess_dialog)
        self.oeqstepbutton_8.setEnabled(True)
        self.oeqstepbutton_8.setGeometry(QtCore.QRect(10, 280, 141, 31))
        self.oeqstepbutton_8.setIcon(icon)
        self.oeqstepbutton_8.setIconSize(QtCore.QSize(20, 20))
        self.oeqstepbutton_8.setCheckable(True)
        self.oeqstepbutton_8.setChecked(False)
        self.oeqstepbutton_8.setAutoRepeat(False)
        self.oeqstepbutton_8.setAutoExclusive(False)
        self.oeqstepbutton_8.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.oeqstepbutton_8.setAutoRaise(False)
        self.oeqstepbutton_8.setArrowType(QtCore.Qt.NoArrow)
        self.oeqstepbutton_8.setObjectName(_fromUtf8("oeqstepbutton_8"))
        self.oeqstepbutton_9 = QtGui.QToolButton(MainstayProcess_dialog)
        self.oeqstepbutton_9.setEnabled(True)
        self.oeqstepbutton_9.setGeometry(QtCore.QRect(10, 330, 141, 31))
        self.oeqstepbutton_9.setIcon(icon)
        self.oeqstepbutton_9.setIconSize(QtCore.QSize(20, 20))
        self.oeqstepbutton_9.setCheckable(True)
        self.oeqstepbutton_9.setChecked(False)
        self.oeqstepbutton_9.setAutoRepeat(False)
        self.oeqstepbutton_9.setAutoExclusive(False)
        self.oeqstepbutton_9.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.oeqstepbutton_9.setAutoRaise(False)
        self.oeqstepbutton_9.setArrowType(QtCore.Qt.NoArrow)
        self.oeqstepbutton_9.setObjectName(_fromUtf8("oeqstepbutton_9"))
        self.oeqstepbutton_10 = QtGui.QToolButton(MainstayProcess_dialog)
        self.oeqstepbutton_10.setEnabled(True)
        self.oeqstepbutton_10.setGeometry(QtCore.QRect(10, 380, 141, 31))
        self.oeqstepbutton_10.setIcon(icon)
        self.oeqstepbutton_10.setIconSize(QtCore.QSize(20, 20))
        self.oeqstepbutton_10.setCheckable(True)
        self.oeqstepbutton_10.setChecked(False)
        self.oeqstepbutton_10.setAutoRepeat(False)
        self.oeqstepbutton_10.setAutoExclusive(False)
        self.oeqstepbutton_10.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.oeqstepbutton_10.setAutoRaise(False)
        self.oeqstepbutton_10.setArrowType(QtCore.Qt.NoArrow)
        self.oeqstepbutton_10.setObjectName(_fromUtf8("oeqstepbutton_10"))
        self.label = QtGui.QLabel(MainstayProcess_dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 31, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 30, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 30, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(MainstayProcess_dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 151, 31, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 30, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 30, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(MainstayProcess_dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 311, 31, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 30, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 30, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(MainstayProcess_dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 261, 31, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 30, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 30, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(MainstayProcess_dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 365, 31, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 30, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 30, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 69, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(MainstayProcess_dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 440, 601, 71))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/Udk-OeQ_logo.png")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.process_button_next = QtGui.QPushButton(MainstayProcess_dialog)
        self.process_button_next.setGeometry(QtCore.QRect(570, 410, 20, 20))
        self.process_button_next.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/arrow_right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.process_button_next.setIcon(icon1)
        self.process_button_next.setIconSize(QtCore.QSize(20, 20))
        self.process_button_next.setFlat(True)
        self.process_button_next.setObjectName(_fromUtf8("process_button_next"))
        self.process_button_prev = QtGui.QPushButton(MainstayProcess_dialog)
        self.process_button_prev.setGeometry(QtCore.QRect(550, 410, 20, 20))
        self.process_button_prev.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/arrow_left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.process_button_prev.setIcon(icon2)
        self.process_button_prev.setIconSize(QtCore.QSize(20, 20))
        self.process_button_prev.setFlat(True)
        self.process_button_prev.setObjectName(_fromUtf8("process_button_prev"))

        self.retranslateUi(MainstayProcess_dialog)
        self.process_page.setCurrentIndex(0)
        QtCore.QObject.connect(self.project_basics_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainstayProcess_dialog.update)
        QtCore.QObject.connect(self.investigation_area_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainstayProcess_dialog.update)
        QtCore.QObject.connect(self.building_shapes_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainstayProcess_dialog.update)
        QtCore.QObject.connect(self.sampling_points_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), MainstayProcess_dialog.update)
        QtCore.QObject.connect(self.process_button_next, QtCore.SIGNAL(_fromUtf8("clicked()")), MainstayProcess_dialog.update)
        QtCore.QMetaObject.connectSlotsByName(MainstayProcess_dialog)

    def retranslateUi(self, MainstayProcess_dialog):
        MainstayProcess_dialog.setWindowTitle(_translate("MainstayProcess_dialog", "Open eQuarter Workflow Utility", None))
        self.ol_plugin_installed_chckBox.setText(_translate("MainstayProcess_dialog", "Install the Open Street Map Plugin", None))
        self.project_created_chckBox.setText(_translate("MainstayProcess_dialog", "Create a new project and save it.", None))
        self.osm_layer_loaded_chckBox.setText(_translate("MainstayProcess_dialog", "Open an Open Layers Map", None))
        self.pst_plugin_installed_chckBox.setText(_translate("MainstayProcess_dialog", "Install the PointSamplingTool Plugin", None))
        self.temp_shapefile_created_chckBox.setText(_translate("MainstayProcess_dialog", "Create a new Polygon-Shapelayer", None))
        self.editing_temp_shapefile_started_chckBox.setText(_translate("MainstayProcess_dialog", "Activate the edit mode", None))
        self.investigation_area_selected_chckBox.setText(_translate("MainstayProcess_dialog", "Add new features to cover your investigation area with", None))
        self.editing_temp_shapefile_stopped_chckBox.setText(_translate("MainstayProcess_dialog", "Deactivate the edit mode", None))
        self.raster_loaded_chckBox.setText(_translate("MainstayProcess_dialog", "Load a new (wms) raster-map", None))
        self.extent_clipped_chckBox.setText(_translate("MainstayProcess_dialog", "Export the investigation areas extent as .tif", None))
        self.pyramids_built_chckBox.setText(_translate("MainstayProcess_dialog", "Open the created .tif-file and build pyramids", None))
        self.temp_pointlayer_created_chckBox.setText(_translate("MainstayProcess_dialog", "Create a new Pointlayer", None))
        self.editing_temp_pointlayer_started_chckBox.setText(_translate("MainstayProcess_dialog", "Activate the edit mode", None))
        self.points_of_interest_defined_chckBox.setText(_translate("MainstayProcess_dialog", "Add new features to mark the buildings you want to \n"
"extract information from", None))
        self.editing_temp_pointlayer_stopped_chckBox.setText(_translate("MainstayProcess_dialog", "Deactivate the edit mode", None))
        self.information_sampled_chckBox.setText(_translate("MainstayProcess_dialog", "Use the point-samplin-tool to extract the information", None))
        self.project_basics_btn.setText(_translate("MainstayProcess_dialog", "Project Basics", None))
        self.investigation_area_btn.setText(_translate("MainstayProcess_dialog", "Investigation Area", None))
        self.building_shapes_btn.setText(_translate("MainstayProcess_dialog", "Building Shapes", None))
        self.sampling_points_btn.setText(_translate("MainstayProcess_dialog", "Sampling Points", None))
        self.oeqstepbutton_5.setText(_translate("MainstayProcess_dialog", "Information Layers", None))
        self.oeqstepbutton_6.setText(_translate("MainstayProcess_dialog", "Legend Assignment", None))
        self.oeqstepbutton_7.setText(_translate("MainstayProcess_dialog", "Algorithm Assignment", None))
        self.oeqstepbutton_8.setText(_translate("MainstayProcess_dialog", "Building Calculations", None))
        self.oeqstepbutton_9.setText(_translate("MainstayProcess_dialog", "Quarter Valuation", None))
        self.oeqstepbutton_10.setText(_translate("MainstayProcess_dialog", "Transfer to Database", None))
        self.label.setText(_translate("MainstayProcess_dialog", "⬇︎", None))
        self.label_2.setText(_translate("MainstayProcess_dialog", "⬇︎", None))
        self.label_3.setText(_translate("MainstayProcess_dialog", "⬇︎", None))
        self.label_4.setText(_translate("MainstayProcess_dialog", "⬇︎", None))
        self.label_5.setText(_translate("MainstayProcess_dialog", "⬇︎", None))
        self.process_button_next.setToolTip(_translate("MainstayProcess_dialog", "continue with next step", None))
        self.process_button_prev.setToolTip(_translate("MainstayProcess_dialog", "redo previous step", None))

import resources_rc
