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

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("115-m-o-t-h-e-r.jpg")
        
        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.setAlignment(QtCore.Qt.AlignHCenter)
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        #self.move(300, 200)
        self.showMaximized()
        self.setWindowTitle('Zen Reader')
        self.show()

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()   
