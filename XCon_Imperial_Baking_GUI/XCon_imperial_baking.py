# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'XCon_imperial_baking.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_XCon_Imperial_Baking(object):
    def setupUi(self, XCon_Imperial_Baking):
        XCon_Imperial_Baking.setObjectName("XCon_Imperial_Baking")
        XCon_Imperial_Baking.resize(1272, 735)
        self.centralWidget = QtWidgets.QWidget(XCon_Imperial_Baking)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 3, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 0, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_monitoring = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_monitoring.setObjectName("radioButton_monitoring")
        self.gridLayout_2.addWidget(self.radioButton_monitoring, 0, 2, 1, 1)
        self.pushButton_import = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_import.setObjectName("pushButton_import")
        self.gridLayout_2.addWidget(self.pushButton_import, 0, 4, 1, 1)
        self.lineEdit_data = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_data.setObjectName("lineEdit_data")
        self.gridLayout_2.addWidget(self.lineEdit_data, 0, 1, 1, 1)
        self.pushButton_browse = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.gridLayout_2.addWidget(self.pushButton_browse, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout.addWidget(self.groupBox, 1, 1, 1, 4)
        self.verticalLayout_temp = QtWidgets.QVBoxLayout()
        self.verticalLayout_temp.setSpacing(6)
        self.verticalLayout_temp.setObjectName("verticalLayout_temp")
        self.gridLayout.addLayout(self.verticalLayout_temp, 2, 1, 2, 3)
        self.verticalLayout_pressure = QtWidgets.QVBoxLayout()
        self.verticalLayout_pressure.setSpacing(6)
        self.verticalLayout_pressure.setObjectName("verticalLayout_pressure")
        self.gridLayout.addLayout(self.verticalLayout_pressure, 4, 1, 2, 3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.radioButton_ch_8 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_ch_8.setAutoExclusive(False)
        self.radioButton_ch_8.setObjectName("radioButton_ch_8")
        self.gridLayout_4.addWidget(self.radioButton_ch_8, 7, 0, 1, 1)
        self.radioButton_ch_4 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_ch_4.setAutoExclusive(False)
        self.radioButton_ch_4.setObjectName("radioButton_ch_4")
        self.gridLayout_4.addWidget(self.radioButton_ch_4, 3, 0, 1, 1)
        self.radioButton_ch_6 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_ch_6.setAutoExclusive(False)
        self.radioButton_ch_6.setObjectName("radioButton_ch_6")
        self.gridLayout_4.addWidget(self.radioButton_ch_6, 5, 0, 1, 1)
        self.radioButton_ch_1 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_ch_1.setAutoExclusive(False)
        self.radioButton_ch_1.setObjectName("radioButton_ch_1")
        self.gridLayout_4.addWidget(self.radioButton_ch_1, 0, 0, 1, 1)
        self.radioButton_ch_7 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_ch_7.setAutoExclusive(False)
        self.radioButton_ch_7.setObjectName("radioButton_ch_7")
        self.gridLayout_4.addWidget(self.radioButton_ch_7, 6, 0, 1, 1)
        self.radioButton_ch_2 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_ch_2.setAutoExclusive(False)
        self.radioButton_ch_2.setObjectName("radioButton_ch_2")
        self.gridLayout_4.addWidget(self.radioButton_ch_2, 1, 0, 1, 1)
        self.radioButton_ch_5 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_ch_5.setAutoExclusive(False)
        self.radioButton_ch_5.setObjectName("radioButton_ch_5")
        self.gridLayout_4.addWidget(self.radioButton_ch_5, 4, 0, 1, 1)
        self.radioButton_ch_3 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_ch_3.setAutoExclusive(False)
        self.radioButton_ch_3.setObjectName("radioButton_ch_3")
        self.gridLayout_4.addWidget(self.radioButton_ch_3, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 4, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        XCon_Imperial_Baking.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(XCon_Imperial_Baking)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1272, 26))
        self.menuBar.setObjectName("menuBar")
        XCon_Imperial_Baking.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(XCon_Imperial_Baking)
        self.mainToolBar.setObjectName("mainToolBar")
        XCon_Imperial_Baking.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(XCon_Imperial_Baking)
        self.statusBar.setObjectName("statusBar")
        XCon_Imperial_Baking.setStatusBar(self.statusBar)

        self.retranslateUi(XCon_Imperial_Baking)
        QtCore.QMetaObject.connectSlotsByName(XCon_Imperial_Baking)

    def retranslateUi(self, XCon_Imperial_Baking):
        _translate = QtCore.QCoreApplication.translate
        XCon_Imperial_Baking.setWindowTitle(_translate("XCon_Imperial_Baking", "XCon_Imperial_Baking"))
        self.groupBox.setTitle(_translate("XCon_Imperial_Baking", "GroupBox"))
        self.radioButton_monitoring.setText(_translate("XCon_Imperial_Baking", "Monitoring"))
        self.pushButton_import.setText(_translate("XCon_Imperial_Baking", "go"))
        self.pushButton_browse.setText(_translate("XCon_Imperial_Baking", "Browse"))
        self.radioButton_ch_8.setText(_translate("XCon_Imperial_Baking", "Channel 8"))
        self.radioButton_ch_4.setText(_translate("XCon_Imperial_Baking", "Channel 4"))
        self.radioButton_ch_6.setText(_translate("XCon_Imperial_Baking", "Channel 6"))
        self.radioButton_ch_1.setText(_translate("XCon_Imperial_Baking", "Channel 1"))
        self.radioButton_ch_7.setText(_translate("XCon_Imperial_Baking", "Channel 7"))
        self.radioButton_ch_2.setText(_translate("XCon_Imperial_Baking", "Channel 2"))
        self.radioButton_ch_5.setText(_translate("XCon_Imperial_Baking", "Channel 5"))
        self.radioButton_ch_3.setText(_translate("XCon_Imperial_Baking", "Channel 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    XCon_Imperial_Baking = QtWidgets.QMainWindow()
    ui = Ui_XCon_Imperial_Baking()
    ui.setupUi(XCon_Imperial_Baking)
    XCon_Imperial_Baking.show()
    sys.exit(app.exec_())

