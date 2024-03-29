# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designCoordy.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(598, 572)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: white\n"
"}\n"
"QScrollBar:vertical {              \n"
"    background: #e5e5ea;\n"
"    border-radius: 3;\n"
"    border: none;\n"
"    max-width: 8px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #196dff;\n"
"    border-radius: 3;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #3b83ff; \n"
"    min-height: 0px;\n"
"    border-radius: 3;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"    background: #e5e5ea;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {              \n"
"    background: #e5e5ea;\n"
"    border-radius: 3;\n"
"    border: none;\n"
"    max-height: 8px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #196dff;\n"
"    border-radius: 3;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #3b83ff; \n"
"    min-height: 0px;\n"
"    border-radius: 3;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"    background: #e5e5ea;\n"
"    border: none;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background: transparent;\n"
"    border-radius: 6;\n"
"    border: none;\n"
"    outline:0px;\n"
"    selection-background-color: white;\n"
"    selection-color: #196dff;\n"
"    padding: 8 0 8 0;\n"
"}")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #fff;")
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFile.setGeometry(QtCore.QRect(250, 620, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnOpenFile.setFont(font)
        self.btnOpenFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnOpenFile.setStyleSheet("QPushButton{\n"
"    background-color:rgba(112, 215, 255, 0);\n"
"    color:rgba(0, 0, 0, 0.5);\n"
"    border: none;\n"
"    border-radius: 5;\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"    color: black;\n"
"}\n"
"")
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.btnAddAltitude = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddAltitude.setGeometry(QtCore.QRect(380, 10, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnAddAltitude.setFont(font)
        self.btnAddAltitude.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAddAltitude.setStyleSheet("QPushButton{\n"
"    background-color:rgba(112, 215, 255, 0);\n"
"    color:rgba(0, 0, 0, 0.5);\n"
"    border: none;\n"
"    border-radius: 5;\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"    color: black;\n"
"}\n"
"")
        self.btnAddAltitude.setObjectName("btnAddAltitude")
        self.btnPolygon = QtWidgets.QPushButton(self.centralwidget)
        self.btnPolygon.setGeometry(QtCore.QRect(30, 40, 250, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnPolygon.setFont(font)
        self.btnPolygon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPolygon.setStyleSheet("QPushButton{\n"
"    background-color: rgba(229,229,234,1);\n"
"    color: #196dff;\n"
"    border: none;\n"
"    border-radius: 12;\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #dceaff; \n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgba(25, 109, 255, 0.7); \n"
"    border-radius: 12;\n"
"}")
        self.btnPolygon.setObjectName("btnPolygon")
        self.btnSaveCsv = QtWidgets.QPushButton(self.centralwidget)
        self.btnSaveCsv.setGeometry(QtCore.QRect(310, 482, 250, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.btnSaveCsv.setFont(font)
        self.btnSaveCsv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSaveCsv.setStyleSheet("QPushButton{\n"
"    background-color: #196dff;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 12;\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #3b83ff; \n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    border-radius: 12;\n"
"}")
        self.btnSaveCsv.setCheckable(False)
        self.btnSaveCsv.setChecked(False)
        self.btnSaveCsv.setObjectName("btnSaveCsv")
        self.btnTxt = QtWidgets.QPushButton(self.centralwidget)
        self.btnTxt.setGeometry(QtCore.QRect(310, 40, 250, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnTxt.setFont(font)
        self.btnTxt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTxt.setStyleSheet("QPushButton{\n"
"    background-color: rgba(229,229,234,1);\n"
"    color: #196dff;\n"
"    border: none;\n"
"    border-radius: 12;\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #dceaff; \n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgba(25, 109, 255, 0.7); \n"
"    border-radius: 12;\n"
"}")
        self.btnTxt.setObjectName("btnTxt")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(30, 150, 531, 300))
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setTabletTracking(True)
        self.graphicsView.setStyleSheet("\n"
"    background-color:rgba(229,229,234,1); \n"
"    border-radius: 6;\n"
"    border: none;\n"
"    padding: 8 4 8 8;\n"
"\n"
"")
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.graphicsView.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setObjectName("graphicsView")
        self.btnSavePointsPolygon = QtWidgets.QPushButton(self.centralwidget)
        self.btnSavePointsPolygon.setGeometry(QtCore.QRect(31, 482, 250, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.btnSavePointsPolygon.setFont(font)
        self.btnSavePointsPolygon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSavePointsPolygon.setStyleSheet("QPushButton{\n"
"    background-color: #196dff;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 12;\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #3b83ff; \n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    border-radius: 12;\n"
"}")
        self.btnSavePointsPolygon.setCheckable(False)
        self.btnSavePointsPolygon.setChecked(False)
        self.btnSavePointsPolygon.setObjectName("btnSavePointsPolygon")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(31, 120, 531, 22))
        self.horizontalSlider.setMinimum(5)
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.labelCountPoint = QtWidgets.QLabel(self.centralwidget)
        self.labelCountPoint.setGeometry(QtCore.QRect(30, 86, 531, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelCountPoint.setFont(font)
        self.labelCountPoint.setStyleSheet("background-color: rgba(255,255,255,0); ")
        self.labelCountPoint.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelCountPoint.setScaledContents(False)
        self.labelCountPoint.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCountPoint.setObjectName("labelCountPoint")
        self.btnMinStep = QtWidgets.QPushButton(self.centralwidget)
        self.btnMinStep.setGeometry(QtCore.QRect(27, 93, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnMinStep.setFont(font)
        self.btnMinStep.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMinStep.setStyleSheet("QPushButton{\n"
"    background-color:rgba(112, 215, 255, 0);\n"
"    color:rgba(0, 0, 0, 0.5);\n"
"    border: none;\n"
"    border-radius: 5;\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"    color: black;\n"
"}\n"
"")
        self.btnMinStep.setObjectName("btnMinStep")
        self.btnMaxStep = QtWidgets.QPushButton(self.centralwidget)
        self.btnMaxStep.setGeometry(QtCore.QRect(526, 93, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btnMaxStep.setFont(font)
        self.btnMaxStep.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMaxStep.setStyleSheet("QPushButton{\n"
"    background-color:rgba(112, 215, 255, 0);\n"
"    color:rgba(0, 0, 0, 0.5);\n"
"    border: none;\n"
"    border-radius: 5;\n"
"    border-style: outset;\n"
"}\n"
"QPushButton:hover{\n"
"    color: black;\n"
"}\n"
"")
        self.btnMaxStep.setObjectName("btnMaxStep")
        self.labelLoading = QtWidgets.QLabel(self.centralwidget)
        self.labelLoading.setGeometry(QtCore.QRect(30, 440, 531, 51))
        self.labelLoading.setToolTip("")
        self.labelLoading.setStyleSheet("background-color:rgba(112, 215, 255, 0);")
        self.labelLoading.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoading.setObjectName("labelLoading")
        self.btnOpenFile.raise_()
        self.btnAddAltitude.raise_()
        self.btnPolygon.raise_()
        self.btnSaveCsv.raise_()
        self.btnTxt.raise_()
        self.btnSavePointsPolygon.raise_()
        self.horizontalSlider.raise_()
        self.labelCountPoint.raise_()
        self.btnMinStep.raise_()
        self.btnMaxStep.raise_()
        self.labelLoading.raise_()
        self.graphicsView.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Coordy"))
        self.btnOpenFile.setToolTip(_translate("MainWindow", "Открыть созданный отчет PDF"))
        self.btnOpenFile.setText(_translate("MainWindow", "Открыть"))
        self.btnAddAltitude.setToolTip(_translate("MainWindow", "Загрузка CSV файла с почасовой выработкой"))
        self.btnAddAltitude.setText(_translate("MainWindow", "Добавление высоты"))
        self.btnPolygon.setToolTip(_translate("MainWindow", "Загрузка исходного контура .kml"))
        self.btnPolygon.setText(_translate("MainWindow", "Загрузить контур"))
        self.btnSaveCsv.setToolTip(_translate("MainWindow", "Сохранение csv файла для дальнейшего импорта в PVsyst"))
        self.btnSaveCsv.setText(_translate("MainWindow", "Сохранить csv для PVsyst"))
        self.btnTxt.setToolTip(_translate("MainWindow", "Загрузка файла .txt с добавленными высотами, с сайта"))
        self.btnTxt.setText(_translate("MainWindow", "Загрузить координаты"))
        self.btnSavePointsPolygon.setToolTip(_translate("MainWindow", "Сохранение подобранной конфигурации в файл .kml"))
        self.btnSavePointsPolygon.setText(_translate("MainWindow", "Сохранить точки + контур"))
        self.labelCountPoint.setText(_translate("MainWindow", "Количество точек"))
        self.btnMinStep.setToolTip(_translate("MainWindow", "Минимальное число точек"))
        self.btnMinStep.setText(_translate("MainWindow", "min"))
        self.btnMaxStep.setToolTip(_translate("MainWindow", "Максимальное число точек"))
        self.btnMaxStep.setText(_translate("MainWindow", "max"))
        self.labelLoading.setText(_translate("MainWindow", "TextLabel"))
