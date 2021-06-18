# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clone.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from datetime import datetime
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

class Ui_MainWindow(object):
    def __init__(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateValue)
        self.timer.start(50)
    def updateValue(self):
        time = datetime.now()
        date = '{} {} {}'.format(time.day, time.strftime('%b'), time.year)
        clock = '{}:{}'.format(time.strftime('%H'), time.strftime('%M'))
        weekDay = time.strftime('%A')
        hum, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        self.label_title.setText(date)
        self.label_clock.setText(clock)
        self.label_weekDay.setText(weekDay)
        self.labelTemp.setText('{:0.1f}'.format(temp))
        self.labelHum.setText('{:0.1f}'.format(hum))
        print('Temp: {:0.1f}*C, Hum: {:0.1f}%'.format(temp, hum))

        tempColor = 'rgba(139, 233, 233, 255)'
        humColor = 'rgba(255, 85, 85, 255)'
        styleSheet = """
        QFrame{
	border-radius: 110px;	
	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} {COLOR}, stop:{STOP_2} rgba(255, 255, 255, 0));
}
        """
        tempPercent = (100-temp)/100.0
        stop_2 = str(tempPercent-0.001)
        stop_1 = str(tempPercent)
        if temp == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace(
            "{STOP_2}", stop_2).replace("{COLOR}", tempColor)
        self.circularTemp.setStyleSheet(newStylesheet)

        humPercent = (100-hum)/100.0
        stop_2 = str(humPercent-0.001)
        stop_1 = str(humPercent)
        if temp == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace(
            "{STOP_2}", stop_2).replace("{COLOR}", humColor)
        self.circularHum.setStyleSheet(newStylesheet)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 480)
        MainWindow.setMinimumSize(QtCore.QSize(760, 480))
        MainWindow.setMaximumSize(QtCore.QSize(760, 480))
        MainWindow.setStyleSheet("background-color: rgb(40, 42, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.circularTempBar_Main = QtWidgets.QFrame(self.centralwidget)
        self.circularTempBar_Main.setGeometry(QtCore.QRect(70, 120, 240, 240))
        self.circularTempBar_Main.setStyleSheet("background-color: none;")
        self.circularTempBar_Main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularTempBar_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularTempBar_Main.setObjectName("circularTempBar_Main")
        self.circularTemp = QtWidgets.QFrame(self.circularTempBar_Main)
        self.circularTemp.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularTemp.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.400 rgba(139, 233, 233, 255), stop:0.395 rgba(255, 255, 255, 0));\n"
"}\n"
"rgb(139, 233, 253)")
        self.circularTemp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularTemp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularTemp.setObjectName("circularTemp")
        self.circularBg = QtWidgets.QFrame(self.circularTempBar_Main)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularBg.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.circularContainer = QtWidgets.QFrame(self.circularTempBar_Main)
        self.circularContainer.setGeometry(QtCore.QRect(25, 25, 190, 190))
        self.circularContainer.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(98, 114, 164);\n"
"}")
        self.circularContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer.setObjectName("circularContainer")
        self.layoutWidget = QtWidgets.QWidget(self.circularContainer)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 171, 137))
        self.layoutWidget.setObjectName("layoutWidget")
        self.timeLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.timeLayout.setContentsMargins(0, 0, 0, 0)
        self.timeLayout.setObjectName("timeLayout")
        self.labelAplicationName = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(10)
        self.labelAplicationName.setFont(font)
        self.labelAplicationName.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelAplicationName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAplicationName.setObjectName("labelAplicationName")
        self.timeLayout.addWidget(self.labelAplicationName, 0, 0, 1, 1)
        self.labelTemp = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(45)
        self.labelTemp.setFont(font)
        self.labelTemp.setStyleSheet("color: rgb(139, 233, 253); padding: 0px; background-color: none;")
        self.labelTemp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTemp.setIndent(-1)
        self.labelTemp.setObjectName("labelTemp")
        self.timeLayout.addWidget(self.labelTemp, 1, 0, 1, 1)
        self.labelCredits = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(8)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet("color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits.setObjectName("labelCredits")
        self.timeLayout.addWidget(self.labelCredits, 2, 0, 1, 1)
        self.circularBg.raise_()
        self.circularTemp.raise_()
        self.circularContainer.raise_()
        self.circularHumBar_Main = QtWidgets.QFrame(self.centralwidget)
        self.circularHumBar_Main.setGeometry(QtCore.QRect(450, 120, 240, 240))
        self.circularHumBar_Main.setStyleSheet("background-color: none;")
        self.circularHumBar_Main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularHumBar_Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularHumBar_Main.setObjectName("circularHumBar_Main")
        self.circularHum = QtWidgets.QFrame(self.circularHumBar_Main)
        self.circularHum.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularHum.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.750 rgba(255, 85, 85, 255), stop:0.745 rgba(255, 255, 255, 0));\n"
"}")
        self.circularHum.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularHum.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularHum.setObjectName("circularHum")
        self.circularHumBg = QtWidgets.QFrame(self.circularHumBar_Main)
        self.circularHumBg.setGeometry(QtCore.QRect(10, 10, 220, 220))
        self.circularHumBg.setStyleSheet("QFrame{\n"
"    border-radius: 110px;    \n"
"    background-color: rgba(85, 85, 127, 100);\n"
"}")
        self.circularHumBg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularHumBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularHumBg.setObjectName("circularHumBg")
        self.circularContainer_3 = QtWidgets.QFrame(self.circularHumBar_Main)
        self.circularContainer_3.setGeometry(QtCore.QRect(25, 25, 190, 190))
        self.circularContainer_3.setBaseSize(QtCore.QSize(0, 0))
        self.circularContainer_3.setStyleSheet("QFrame{\n"
"    border-radius: 95px;    \n"
"    background-color: rgb(98, 114, 164);\n"
"}")
        self.circularContainer_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circularContainer_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularContainer_3.setObjectName("circularContainer_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.circularContainer_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 40, 171, 137))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.infoLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.infoLayout_3.setContentsMargins(0, 0, 0, 0)
        self.infoLayout_3.setObjectName("infoLayout_3")
        self.labelAplicationName_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(10)
        self.labelAplicationName_3.setFont(font)
        self.labelAplicationName_3.setStyleSheet("color: #FFFFFF; background-color: none;")
        self.labelAplicationName_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAplicationName_3.setObjectName("labelAplicationName_3")
        self.infoLayout_3.addWidget(self.labelAplicationName_3, 0, 0, 1, 1)
        self.labelHum = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(45)
        self.labelHum.setFont(font)
        self.labelHum.setStyleSheet("color: rgb(255, 85, 85); padding: 0px; background-color: none;")
        self.labelHum.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHum.setIndent(-1)
        self.labelHum.setObjectName("labelHum")
        self.infoLayout_3.addWidget(self.labelHum, 1, 0, 1, 1)
        self.labelCredits_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(8)
        self.labelCredits_3.setFont(font)
        self.labelCredits_3.setStyleSheet("color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits_3.setObjectName("labelCredits_3")
        self.infoLayout_3.addWidget(self.labelCredits_3, 2, 0, 1, 1)
        self.circularHumBg.raise_()
        self.circularHum.raise_()
        self.circularContainer_3.raise_()
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(60, 10, 641, 50))
        self.label_title.setStyleSheet("color: rgb(248, 248, 242); background-color: none; font-size: 22px;")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_weekDay = QtWidgets.QLabel(self.centralwidget)
        self.label_weekDay.setGeometry(QtCore.QRect(210, 60, 341, 16))
        self.label_weekDay.setStyleSheet("color: rgb(248, 248, 242); font-size: 12px; padding-left: 2px; padding-right: 2px; border: none;")
        self.label_weekDay.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weekDay.setObjectName("label_weekDay")
        self.label_clock = QtWidgets.QLabel(self.centralwidget)
        self.label_clock.setGeometry(QtCore.QRect(260, 90, 241, 16))
        self.label_clock.setStyleSheet("color: rgb(248, 248, 242); font-size: 12px; padding-left: 2px; padding-right: 2px; border: none;")
        self.label_clock.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clock.setObjectName("label_clock")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DHT22 Monitor"))
        self.labelAplicationName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">TEMPERATURE</span></p></body></html>"))
        self.labelTemp.setText(_translate("MainWindow", "60°C"))
        self.labelCredits.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.labelAplicationName_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">HUMIDITY</span></p></body></html>"))
        self.labelHum.setText(_translate("MainWindow", "25%"))
        self.labelCredits_3.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_title.setText(_translate("MainWindow", "DD Mmm YYYY"))
        self.label_weekDay.setText(_translate("MainWindow", "weekDay"))
        self.label_clock.setText(_translate("MainWindow", "HH:MM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

