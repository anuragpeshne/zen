#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import os
from os import listdir
import random

class Reader(QtGui.QWidget):
    def __init__(self):
        super(Reader, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.initUI()
        
    def initUI(self):      
        self.listDir = os.listdir()
        self.curPic = 1;
    
        hbox = QtGui.QHBoxLayout(self)
        hbox.setMargin(0)     
        
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setAlignment(QtCore.Qt.AlignHCenter)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.setNextPic()
        
        self.vbar = self.scrollArea.verticalScrollBar()
        print(self.scrollArea.height())

        hbox.addWidget(self.scrollArea)
        self.setLayout(hbox)
        
        self.showMaximized()
        self.setWindowTitle('Zen Reader')
        self.show()

    def scroll(self):
        ht = self.height()
        self.scrollHt = self.scrollHt + ht/3
        print(self.vbar.value())
        print(self.height())
        print(self.pixmap.height())
        if(self.vbar.value() + self.height() >= self.pixmap.height()):
            self.vbar.setValue(0)
            self.scrollHt = 0
        else:
            #animation = QtCore.QPropertyAnimation(self.scrollArea, "geometry");
            #animation.setDuration(10000);
            #animation.setStartValue(QRect(0, 0, 100, 30));
            #animation.setEndValue(QRect(250, 250, 100, 30));

            #animation.start();
            self.vbar.setValue(self.scrollHt)

    def setNextPic(self):
        while True:
            rnd = random.randrange(0,len(self.listDir))
            tempFileName = self.listDir[rnd]
            if tempFileName[-3:] != ".py":
                self.pixmap = QtGui.QPixmap(self.listDir[rnd])
                break
        self.lbl = QtGui.QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.scrollArea.setWidget(self.lbl)
        self.scrollHt = 0
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.setNextPic()
            
        else:
            self.scroll()

    def keyPressEvent(self, event):
         if event.key() == QtCore.Qt.Key_Escape:
            self.close()

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Reader()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()   
