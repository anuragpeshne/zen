#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we dispay an image
on the window. 

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

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

        self.lbl = QtGui.QLabel(self)
        self.setNextPic()
        
        scrollArea = QtGui.QScrollArea(self)
        scrollArea.setWidget(self.lbl)
        scrollArea.setAlignment(QtCore.Qt.AlignHCenter)
        scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollHt = 1
        
        self.vbar = scrollArea.verticalScrollBar()
        print(scrollArea.height())

        hbox.addWidget(scrollArea)
        self.setLayout(hbox)
        
        self.showMaximized()
        self.setWindowTitle('Zen Reader')
        self.show()

    def scroll(self):
        ht = self.height()
        self.scrollHt = self.scrollHt + ht/2
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
        rnd = random.randrange(0,len(self.listDir))
        self.pixmap = QtGui.QPixmap(self.listDir[rnd])
        self.lbl.setPixmap(self.pixmap)
        self.scrollHt = 0
        
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.setNextPic()
            
        else:
            self.scroll()

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Reader()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()   
