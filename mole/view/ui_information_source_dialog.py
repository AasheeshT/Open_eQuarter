# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/ui_information_source_dialog.ui'
#
# Created: Sat Aug 15 12:43:35 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_InformationSource_dialog(object):
    def setupUi(self, InformationSource_dialog):
        InformationSource_dialog.setObjectName(_fromUtf8("InformationSource_dialog"))
        InformationSource_dialog.resize(457, 421)
        InformationSource_dialog.setStyleSheet(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(InformationSource_dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridWidget = QtGui.QWidget(InformationSource_dialog)
        self.gridWidget.setStyleSheet(_fromUtf8("QPushButton {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QLabel {\n"
"    margin-top: 2px;\n"
"}\n"
"\n"
"#blind1 {\n"
"    border: none;\n"
"    color: rgb(237, 237, 237);\n"
"}\n"
"\n"
"#blind2 {\n"
"    border: none;\n"
"    color: rgb(237, 237, 237);\n"
"}\n"
"\n"
"#blind3 {\n"
"    border: none;\n"
"    color: rgb(237, 237, 237);\n"
"}\n"
"\n"
"#blind4 {\n"
"    border: none;\n"
"    color: rgb(237, 237, 237);\n"
"}"))
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.grid = QtGui.QGridLayout(self.gridWidget)
        self.grid.setMargin(0)
        self.grid.setVerticalSpacing(0)
        self.grid.setObjectName(_fromUtf8("grid"))
        self.layer_name = QtGui.QLineEdit(self.gridWidget)
        self.layer_name.setObjectName(_fromUtf8("layer_name"))
        self.grid.addWidget(self.layer_name, 3, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.grid.addWidget(self.label_11, 3, 0, 1, 1)
        self.blind2 = QtGui.QPushButton(self.gridWidget)
        self.blind2.setMaximumSize(QtCore.QSize(21, 21))
        self.blind2.setText(_fromUtf8(""))
        self.blind2.setFlat(False)
        self.blind2.setObjectName(_fromUtf8("blind2"))
        self.grid.addWidget(self.blind2, 7, 2, 1, 1)
        self.blind1 = QtGui.QPushButton(self.gridWidget)
        self.blind1.setMaximumSize(QtCore.QSize(21, 21))
        self.blind1.setText(_fromUtf8(""))
        self.blind1.setCheckable(False)
        self.blind1.setAutoDefault(True)
        self.blind1.setFlat(False)
        self.blind1.setObjectName(_fromUtf8("blind1"))
        self.grid.addWidget(self.blind1, 3, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.grid.addWidget(self.label_8, 11, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.grid.addWidget(self.label_6, 8, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.gridWidget)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.grid.addWidget(self.label_12, 0, 0, 1, 3)
        self.wms = QtGui.QLineEdit(self.gridWidget)
        self.wms.setObjectName(_fromUtf8("wms"))
        self.grid.addWidget(self.wms, 7, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.grid.addWidget(self.label_7, 10, 0, 1, 1)
        self.open_dxf_btn = QtGui.QPushButton(self.gridWidget)
        self.open_dxf_btn.setMaximumSize(QtCore.QSize(21, 21))
        self.open_dxf_btn.setObjectName(_fromUtf8("open_dxf_btn"))
        self.grid.addWidget(self.open_dxf_btn, 12, 2, 1, 1)
        self.extension_dropdown = QtGui.QComboBox(self.gridWidget)
        self.extension_dropdown.setMaximumSize(QtCore.QSize(16777215, 26))
        self.extension_dropdown.setObjectName(_fromUtf8("extension_dropdown"))
        self.grid.addWidget(self.extension_dropdown, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.grid.addWidget(self.label_2, 6, 0, 1, 3)
        self.wfs = QtGui.QLineEdit(self.gridWidget)
        self.wfs.setObjectName(_fromUtf8("wfs"))
        self.grid.addWidget(self.wfs, 11, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.grid.addWidget(self.label_9, 12, 0, 1, 1)
        self.shapefile = QtGui.QLineEdit(self.gridWidget)
        self.shapefile.setObjectName(_fromUtf8("shapefile"))
        self.grid.addWidget(self.shapefile, 10, 1, 1, 1)
        self.open_csv_btn = QtGui.QPushButton(self.gridWidget)
        self.open_csv_btn.setMaximumSize(QtCore.QSize(21, 21))
        self.open_csv_btn.setObjectName(_fromUtf8("open_csv_btn"))
        self.grid.addWidget(self.open_csv_btn, 14, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 25))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.grid.addWidget(self.label_4, 13, 0, 1, 3)
        self.open_geotiff_btn = QtGui.QPushButton(self.gridWidget)
        self.open_geotiff_btn.setMaximumSize(QtCore.QSize(21, 21))
        self.open_geotiff_btn.setObjectName(_fromUtf8("open_geotiff_btn"))
        self.grid.addWidget(self.open_geotiff_btn, 8, 2, 1, 1)
        self.open_shapefile_btn = QtGui.QPushButton(self.gridWidget)
        self.open_shapefile_btn.setMaximumSize(QtCore.QSize(21, 21))
        self.open_shapefile_btn.setObjectName(_fromUtf8("open_shapefile_btn"))
        self.grid.addWidget(self.open_shapefile_btn, 10, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridWidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.grid.addWidget(self.label_3, 9, 0, 1, 3)
        self.label = QtGui.QLabel(self.gridWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label.setObjectName(_fromUtf8("label"))
        self.grid.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.grid.addWidget(self.label_5, 7, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.grid.addWidget(self.label_10, 14, 0, 1, 1)
        self.csv = QtGui.QLineEdit(self.gridWidget)
        self.csv.setObjectName(_fromUtf8("csv"))
        self.grid.addWidget(self.csv, 14, 1, 1, 1)
        self.geotiff = QtGui.QLineEdit(self.gridWidget)
        self.geotiff.setObjectName(_fromUtf8("geotiff"))
        self.grid.addWidget(self.geotiff, 8, 1, 1, 1)
        self.blind3 = QtGui.QPushButton(self.gridWidget)
        self.blind3.setMaximumSize(QtCore.QSize(21, 21))
        self.blind3.setText(_fromUtf8(""))
        self.blind3.setFlat(False)
        self.blind3.setObjectName(_fromUtf8("blind3"))
        self.grid.addWidget(self.blind3, 11, 2, 1, 1)
        self.dxf = QtGui.QLineEdit(self.gridWidget)
        self.dxf.setObjectName(_fromUtf8("dxf"))
        self.grid.addWidget(self.dxf, 12, 1, 1, 1)
        self.field_id = QtGui.QLineEdit(self.gridWidget)
        self.field_id.setObjectName(_fromUtf8("field_id"))
        self.grid.addWidget(self.field_id, 2, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.gridWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.grid.addWidget(self.label_13, 2, 0, 1, 1)
        self.blind4 = QtGui.QPushButton(self.gridWidget)
        self.blind4.setMaximumSize(QtCore.QSize(21, 21))
        self.blind4.setText(_fromUtf8(""))
        self.blind4.setObjectName(_fromUtf8("blind4"))
        self.grid.addWidget(self.blind4, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.gridWidget)
        self.buttonBox = QtGui.QDialogButtonBox(InformationSource_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(InformationSource_dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), InformationSource_dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), InformationSource_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InformationSource_dialog)

    def retranslateUi(self, InformationSource_dialog):
        InformationSource_dialog.setWindowTitle(_translate("InformationSource_dialog", "Dialog", None))
        self.label_11.setText(_translate("InformationSource_dialog", "Layer name:", None))
        self.label_8.setText(_translate("InformationSource_dialog", "WFS", None))
        self.label_6.setText(_translate("InformationSource_dialog", "GeoTiff", None))
        self.label_12.setText(_translate("InformationSource_dialog", "Load information source", None))
        self.label_7.setText(_translate("InformationSource_dialog", "SHP", None))
        self.open_dxf_btn.setText(_translate("InformationSource_dialog", "...", None))
        self.label_2.setText(_translate("InformationSource_dialog", "Raster", None))
        self.label_9.setText(_translate("InformationSource_dialog", "DXF", None))
        self.open_csv_btn.setText(_translate("InformationSource_dialog", "...", None))
        self.label_4.setText(_translate("InformationSource_dialog", "Table", None))
        self.open_geotiff_btn.setText(_translate("InformationSource_dialog", "...", None))
        self.open_shapefile_btn.setText(_translate("InformationSource_dialog", "...", None))
        self.label_3.setText(_translate("InformationSource_dialog", "Vector", None))
        self.label.setText(_translate("InformationSource_dialog", "Information type:", None))
        self.label_5.setText(_translate("InformationSource_dialog", "WMS", None))
        self.label_10.setText(_translate("InformationSource_dialog", "CSV", None))
        self.label_13.setText(_translate("InformationSource_dialog", "Field Id:", None))
