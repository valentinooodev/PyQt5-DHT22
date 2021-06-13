# Evolab's project 2021
# Author: Valentinooo


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from datetime import datetime
from random import randint
import gui
#import Adafruit_DHT

# DHT_SENSOR = Adafruit_DHT.DHT22
# DHT_PIN = 4

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateValue)
        self.timer.start(50)

    def updateValue(self):
        time = datetime.now()
        date = '{} {} {}'.format(time.day, time.strftime('%b'), time.year)
        clock = '{}:{}:{}'.format(time.strftime('%H'), time.strftime('%M'), time.strftime('%S'))
        weekDay = time.strftime('%A')
        # hum, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        # hum = '{:.1f}'.format(hum)
        # temp = '{:.1f}'.format(temp)

        self.ui.dateLabel.setText(date)
        self.ui.clockLabel.setText(clock)
        self.ui.weekDayLabel.setText(weekDay)
        # self.ui.humLabel.setText(hum)
        # self.ui.tempLabel.setText(temp)


import sys
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())