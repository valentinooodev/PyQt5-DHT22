# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setStyleSheet("background: rgb(40, 42, 54)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeFrame = QtWidgets.QFrame(self.centralwidget)
        self.timeFrame.setEnabled(False)
        self.timeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timeFrame.setObjectName("timeFrame")
        self.dateLabel = QtWidgets.QLabel(self.timeFrame)
        self.dateLabel.setGeometry(QtCore.QRect(291, 30, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet("color: rgb(255, 121, 198); font: 20pt \"Consolas\";")
        self.dateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.clockLabel = QtWidgets.QLabel(self.timeFrame)
        self.clockLabel.setGeometry(QtCore.QRect(351, 110, 80, 20))
        self.clockLabel.setStyleSheet("color: rgb(255, 121, 198); font: 20pt \"Consolas\";")
        self.clockLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.clockLabel.setObjectName("clockLabel")
        self.dayInWeekLabel = QtWidgets.QLabel(self.timeFrame)
        self.dayInWeekLabel.setGeometry(QtCore.QRect(301, 70, 180, 20))
        self.dayInWeekLabel.setStyleSheet("color: rgb(255, 121, 198); font: 20pt \"Consolas\";")
        self.dayInWeekLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dayInWeekLabel.setObjectName("dayInWeekLabel")
        self.verticalLayout.addWidget(self.timeFrame)
        self.dataFrame = QtWidgets.QFrame(self.centralwidget)
        self.dataFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dataFrame.setObjectName("dataFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dataFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tempFrame = QtWidgets.QFrame(self.dataFrame)
        self.tempFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tempFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tempFrame.setObjectName("tempFrame")
        self.humCircleFrame = QtWidgets.QFrame(self.tempFrame)
        self.humCircleFrame.setGeometry(QtCore.QRect(99, 0, 180, 180))
        self.humCircleFrame.setMaximumSize(QtCore.QSize(180, 180))
        self.humCircleFrame.setStyleSheet("QFrame{\n"
"    border: 5px solid rgb(189, 147, 249);\n"
"    border-radius: 90px;\n"
"}")
        self.humCircleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.humCircleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.humCircleFrame.setObjectName("humCircleFrame")
        self.temperature = QtWidgets.QLabel(self.humCircleFrame)
        self.temperature.setGeometry(QtCore.QRect(45, 20, 90, 12))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.temperature.setFont(font)
        self.temperature.setStyleSheet("border: 0px;\n"
"color: rgb(255, 121, 198);\n"
"font: 12pt \"Consolas\";")
        self.temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature.setObjectName("temperature")
        self.celsius = QtWidgets.QLabel(self.humCircleFrame)
        self.celsius.setGeometry(QtCore.QRect(65, 145, 50, 13))
        self.celsius.setStyleSheet("border: 0px;\n"
"color: rgb(255, 121, 198);\n"
"font: 12pt \"Consolas\";")
        self.celsius.setAlignment(QtCore.Qt.AlignCenter)
        self.celsius.setObjectName("celsius")
        self.tempLabel = QtWidgets.QLabel(self.humCircleFrame)
        self.tempLabel.setGeometry(QtCore.QRect(40, 70, 100, 30))
        self.tempLabel.setStyleSheet("border: 0px; color: rgb(255, 121, 198);font: 30pt \"Consolas\";")
        self.tempLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLabel.setObjectName("tempLabel")
        self.horizontalLayout.addWidget(self.tempFrame)
        self.humFrame = QtWidgets.QFrame(self.dataFrame)
        self.humFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.humFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.humFrame.setObjectName("humFrame")
        self.tempCircleFrame = QtWidgets.QFrame(self.humFrame)
        self.tempCircleFrame.setGeometry(QtCore.QRect(99, 0, 180, 180))
        self.tempCircleFrame.setMaximumSize(QtCore.QSize(180, 180))
        self.tempCircleFrame.setStyleSheet("QFrame{\n"
"    border: 5px solid rgb(189, 147, 249);\n"
"    border-radius: 90px;\n"
"}")
        self.tempCircleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tempCircleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tempCircleFrame.setObjectName("tempCircleFrame")
        self.humidity = QtWidgets.QLabel(self.tempCircleFrame)
        self.humidity.setGeometry(QtCore.QRect(45, 20, 90, 12))
        self.humidity.setStyleSheet("border: 0px;\n"
"color: rgb(255, 121, 198);\n"
"font: 12pt \"Consolas\";")
        self.humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity.setObjectName("humidity")
        self.percent = QtWidgets.QLabel(self.tempCircleFrame)
        self.percent.setGeometry(QtCore.QRect(65, 145, 50, 13))
        self.percent.setStyleSheet("border: 0px;\n"
"color: rgb(255, 121, 198);\n"
"font: 12pt \"Consolas\";")
        self.percent.setAlignment(QtCore.Qt.AlignCenter)
        self.percent.setObjectName("percent")
        self.humLabel = QtWidgets.QLabel(self.tempCircleFrame)
        self.humLabel.setGeometry(QtCore.QRect(40, 70, 100, 30))
        self.humLabel.setStyleSheet("border: 0px; color: rgb(255, 121, 198); font: 30pt \"Consolas\";")
        self.humLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.humLabel.setObjectName("humLabel")
        self.horizontalLayout.addWidget(self.humFrame)
        self.verticalLayout.addWidget(self.dataFrame)
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dateLabel.setText(_translate("MainWindow", "DD Mmm YYYY"))
        self.clockLabel.setText(_translate("MainWindow", "HH:MM"))
        self.dayInWeekLabel.setText(_translate("MainWindow", "Day"))
        self.temperature.setText(_translate("MainWindow", "TEMPATURE"))
        self.celsius.setText(_translate("MainWindow", "°C"))
        self.tempLabel.setText(_translate("MainWindow", "00.0"))
        self.humidity.setText(_translate("MainWindow", "HUMIDITY"))
        self.percent.setText(_translate("MainWindow", "%"))
        self.humLabel.setText(_translate("MainWindow", "00.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
