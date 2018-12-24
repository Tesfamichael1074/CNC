# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './CNCUI.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 697)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(829, 697))
        MainWindow.setMaximumSize(QtCore.QSize(829, 697))
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(10, 0, 25, 19))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Open_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_2.setGeometry(QtCore.QRect(40, 0, 25, 19))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/Add File_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setAutoRaise(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_3.setGeometry(QtCore.QRect(100, 0, 25, 19))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/Pencil_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_4.setGeometry(QtCore.QRect(70, 0, 25, 19))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/Gears_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_4.setIcon(icon3)
        self.toolButton_4.setAutoRaise(True)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_6 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_6.setGeometry(QtCore.QRect(130, 0, 25, 19))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/Erase_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon4)
        self.toolButton_6.setAutoRaise(True)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_8 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_8.setGeometry(QtCore.QRect(160, 0, 25, 19))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/Python_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_8.setIcon(icon5)
        self.toolButton_8.setAutoRaise(True)
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(510, 20, 291, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.toolBox.setPalette(palette)
        self.toolBox.setStyleSheet("color: rgb(0, 85, 0);")
        self.toolBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 291, 89))
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(20, 10, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(40, 30, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 16, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page)
        self.label_6.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.label_6.setObjectName("label_6")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/West Direction_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon6, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 291, 89))
        self.page_2.setObjectName("page_2")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(30, 0, 21, 16))
        self.label_7.setObjectName("label_7")
        self.toolButton_9 = QtWidgets.QToolButton(self.page_2)
        self.toolButton_9.setGeometry(QtCore.QRect(50, 0, 25, 19))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/Chevron Left_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_9.setIcon(icon7)
        self.toolButton_9.setAutoRaise(True)
        self.toolButton_9.setObjectName("toolButton_9")
        self.toolButton_10 = QtWidgets.QToolButton(self.page_2)
        self.toolButton_10.setGeometry(QtCore.QRect(80, 0, 25, 19))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/Chevron Right_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_10.setIcon(icon8)
        self.toolButton_10.setAutoRaise(True)
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_11 = QtWidgets.QToolButton(self.page_2)
        self.toolButton_11.setGeometry(QtCore.QRect(80, 20, 25, 19))
        self.toolButton_11.setIcon(icon8)
        self.toolButton_11.setAutoRaise(True)
        self.toolButton_11.setObjectName("toolButton_11")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(30, 20, 21, 16))
        self.label_8.setObjectName("label_8")
        self.toolButton_12 = QtWidgets.QToolButton(self.page_2)
        self.toolButton_12.setGeometry(QtCore.QRect(50, 20, 25, 19))
        self.toolButton_12.setIcon(icon7)
        self.toolButton_12.setAutoRaise(True)
        self.toolButton_12.setObjectName("toolButton_12")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(120, 0, 41, 16))
        self.label_9.setObjectName("label_9")
        self.spinBox = QtWidgets.QSpinBox(self.page_2)
        self.spinBox.setGeometry(QtCore.QRect(160, 0, 61, 22))
        self.spinBox.setSuffix("")
        self.spinBox.setMaximum(180)
        self.spinBox.setSingleStep(5)
        self.spinBox.setObjectName("spinBox")
        self.dial = QtWidgets.QDial(self.page_2)
        self.dial.setGeometry(QtCore.QRect(160, 20, 51, 51))
        self.dial.setObjectName("dial")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/Game Controller_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_2, icon9, "")
        self.toolBox_2 = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox_2.setGeometry(QtCore.QRect(510, 180, 291, 123))
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 291, 66))
        self.page_3.setObjectName("page_3")
        self.toolButton_13 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_13.setGeometry(QtCore.QRect(10, 0, 25, 19))
        self.toolButton_13.setIcon(icon2)
        self.toolButton_13.setAutoRaise(True)
        self.toolButton_13.setObjectName("toolButton_13")
        self.toolButton_15 = QtWidgets.QToolButton(self.page_3)
        self.toolButton_15.setGeometry(QtCore.QRect(10, 30, 25, 19))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/Type_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_15.setIcon(icon10)
        self.toolButton_15.setAutoRaise(True)
        self.toolButton_15.setObjectName("toolButton_15")
        self.fontComboBox = QtWidgets.QFontComboBox(self.page_3)
        self.fontComboBox.setGeometry(QtCore.QRect(40, 30, 188, 22))
        self.fontComboBox.setObjectName("fontComboBox")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/Hand With Pen_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox_2.addItem(self.page_3, icon11, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 291, 66))
        self.page_4.setObjectName("page_4")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 61, 16))
        self.label_10.setObjectName("label_10")
        self.horizontalSlider = QtWidgets.QSlider(self.page_4)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 0, 181, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setGeometry(QtCore.QRect(250, 0, 47, 13))
        self.label_11.setObjectName("label_11")
        self.toolBox_2.addItem(self.page_4, "")
        self.toolButton_16 = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_16.setGeometry(QtCore.QRect(190, 0, 25, 19))
        self.toolButton_16.setIcon(icon10)
        self.toolButton_16.setAutoRaise(True)
        self.toolButton_16.setObjectName("toolButton_16")
        self.toolBox_3 = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox_3.setGeometry(QtCore.QRect(510, 310, 291, 123))
        self.toolBox_3.setObjectName("toolBox_3")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 291, 69))
        self.page_5.setObjectName("page_5")
        self.pushButton = QtWidgets.QPushButton(self.page_5)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 111, 23))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/WinRAR_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 30, 111, 23))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/Arduino_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon13)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 30, 111, 23))
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/Detective_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon14)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_10.setGeometry(QtCore.QRect(150, 0, 111, 23))
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/Export_50px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon15)
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.toolBox_3.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 291, 69))
        self.page_6.setObjectName("page_6")
        self.toolBox_3.addItem(self.page_6, "")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(0, 30, 481, 411))
        self.img = cv2.imread("ma pic.jpg")
        self.resi = cv2.resize(self.img,(480,500))
        cv2.imwrite('pic2.png',self.resi)
        self.label_12.setPixmap(QPixmap("pic2.png"))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuBoard_Properties = QtWidgets.QMenu(self.menubar)
        self.menuBoard_Properties.setObjectName("menuBoard_Properties")
        self.menuSelect_a_board = QtWidgets.QMenu(self.menuBoard_Properties)
        self.menuSelect_a_board.setObjectName("menuSelect_a_board")
        self.menuSelect_a_Bound_rate = QtWidgets.QMenu(self.menuBoard_Properties)
        self.menuSelect_a_Bound_rate.setObjectName("menuSelect_a_Bound_rate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRecent = QtWidgets.QAction(MainWindow)
        self.actionRecent.setObjectName("actionRecent")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionDraw_Circle = QtWidgets.QAction(MainWindow)
        self.actionDraw_Circle.setObjectName("actionDraw_Circle")
        self.actionDraw_a_line = QtWidgets.QAction(MainWindow)
        self.actionDraw_a_line.setObjectName("actionDraw_a_line")
        self.actionDrraw_an_elipse = QtWidgets.QAction(MainWindow)
        self.actionDrraw_an_elipse.setObjectName("actionDrraw_an_elipse")
        self.actionArduino = QtWidgets.QAction(MainWindow)
        self.actionArduino.setObjectName("actionArduino")
        self.actionRaspberry_PI3 = QtWidgets.QAction(MainWindow)
        self.actionRaspberry_PI3.setObjectName("actionRaspberry_PI3")
        self.actionPIC = QtWidgets.QAction(MainWindow)
        self.actionPIC.setObjectName("actionPIC")
        self.action8051 = QtWidgets.QAction(MainWindow)
        self.action8051.setObjectName("action8051")
        self.action9600 = QtWidgets.QAction(MainWindow)
        self.action9600.setObjectName("action9600")
        self.action10000 = QtWidgets.QAction(MainWindow)
        self.action10000.setObjectName("action10000")
        self.actionCustom = QtWidgets.QAction(MainWindow)
        self.actionCustom.setObjectName("actionCustom")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRecent)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionPrint)
        self.menuEdit.addAction(self.actionDraw_Circle)
        self.menuEdit.addAction(self.actionDraw_a_line)
        self.menuEdit.addAction(self.actionDrraw_an_elipse)
        self.menuSelect_a_board.addAction(self.actionArduino)
        self.menuSelect_a_board.addAction(self.actionRaspberry_PI3)
        self.menuSelect_a_board.addAction(self.actionPIC)
        self.menuSelect_a_board.addAction(self.action8051)
        self.menuSelect_a_Bound_rate.addAction(self.action9600)
        self.menuSelect_a_Bound_rate.addAction(self.action10000)
        self.menuSelect_a_Bound_rate.addAction(self.actionCustom)
        self.menuBoard_Properties.addAction(self.menuSelect_a_board.menuAction())
        self.menuBoard_Properties.addAction(self.menuSelect_a_Bound_rate.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuBoard_Properties.menuAction())
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setValue(0)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(2)
        self.toolBox_2.setCurrentIndex(1)
        self.toolBox_3.setCurrentIndex(0)
        self.toolButton.clicked.connect(self.label_8.clear)
        self.horizontalSlider.rangeChanged['int','int'].connect(self.label_11.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.horizontalSlider.valueChanged.connect(self.image1)
        self.pushButton_3.clicked.connect(self.thresholder)

    def thresholder(self):
        #ma = cv2.imread("pic2.jpg")
        _, threshimg = cv2.threshold(self.resi1,25,255,cv2.THRESH_BINARY_INV)
        print("thresh is ended")
        cv2.imwrite('tesfa.png',threshimg)
        print("writing is ended")
        self.label_12.setPixmap(QPixmap("tesfa.png"))
        cv2.imshow("drawing",threshimg)


    def image1(self):
        
        x = self.horizontalSlider.value()
        self.label_11.setText(str(x))
        self.resi1 = cv2.Canny(self.resi,10,x)
        cv2.imwrite('pic2.png',self.resi1)
        self.label_12.setPixmap(QPixmap("pic2.png"))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CNC"))
        self.toolButton_2.setText(_translate("MainWindow", "..."))
        self.toolButton_3.setText(_translate("MainWindow", "..."))
        self.toolButton_4.setText(_translate("MainWindow", "..."))
        self.toolButton_6.setText(_translate("MainWindow", "..."))
        self.toolButton_8.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "X = "))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Y = "))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "Z = "))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Axis"))
        self.label_7.setText(_translate("MainWindow", "X - "))
        self.toolButton_9.setText(_translate("MainWindow", "..."))
        self.toolButton_10.setText(_translate("MainWindow", "..."))
        self.toolButton_11.setText(_translate("MainWindow", "..."))
        self.label_8.setText(_translate("MainWindow", "Y - "))
        self.toolButton_12.setText(_translate("MainWindow", "..."))
        self.label_9.setText(_translate("MainWindow", "Servo - "))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Test"))
        self.toolBox.setItemToolTip(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "<html><head/><body><p>this is to test the motors</p></body></html>"))
        self.toolButton_13.setText(_translate("MainWindow", "..."))
        self.toolButton_15.setText(_translate("MainWindow", "..."))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), _translate("MainWindow", "Free scetch"))
        self.label_10.setText(_translate("MainWindow", "edges"))
        self.label_11.setText(_translate("MainWindow", "0%"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_4), _translate("MainWindow", "Ajustments"))
        self.toolButton_16.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Extract image"))
        self.pushButton_2.setText(_translate("MainWindow", "Deploy image"))
        self.pushButton_3.setText(_translate("MainWindow", "Drawing view"))
        self.pushButton_10.setText(_translate("MainWindow", "Export drawing"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_5), _translate("MainWindow", "Deployment"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_6), _translate("MainWindow", "Page 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuBoard_Properties.setTitle(_translate("MainWindow", "Board Properties"))
        self.menuSelect_a_board.setTitle(_translate("MainWindow", "Select a board"))
        self.menuSelect_a_Bound_rate.setTitle(_translate("MainWindow", "Select a Bound rate"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionRecent.setText(_translate("MainWindow", "Recent"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionDraw_Circle.setText(_translate("MainWindow", "Draw Circle"))
        self.actionDraw_a_line.setText(_translate("MainWindow", "Draw a line"))
        self.actionDrraw_an_elipse.setText(_translate("MainWindow", "Drraw an elipse"))
        self.actionArduino.setText(_translate("MainWindow", "Arduino"))
        self.actionRaspberry_PI3.setText(_translate("MainWindow", "Raspberry PI3"))
        self.actionPIC.setText(_translate("MainWindow", "PIC"))
        self.action8051.setText(_translate("MainWindow", "8051"))
        self.action9600.setText(_translate("MainWindow", "9600"))
        self.action10000.setText(_translate("MainWindow", "10000"))
        self.actionCustom.setText(_translate("MainWindow", "Custom"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
