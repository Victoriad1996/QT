from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtCore import Qt, QPoint

from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5 import QtWidgets, QtCore, QtGui
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(30,30,600,400)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

        self.brushColor = Qt.black
        self.brushSize = 2


        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        #self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setBrush(QtGui.QBrush(QtGui.QColor(100, 10, 10, 40)))
        qp.drawLine(self.begin, self.end)

    def paintingLine(self):
        qp = QtGui.QPainter(self)
        qp.setBrush(QtGui.QBrush(QtGui.QColor(100, 10, 10, 40)))
        qp.drawLine(self.begin, self.end)
        print("paintevent")
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.begin = event.pos()
            self.end = event.pos()
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            self.end = event.pos()

            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            #self.begin = event.pos()
            self.drawing = False
            self.end = event.pos()
            qp = QtGui.QPainter(self.image)
            qp.setBrush(QtGui.QBrush(QtGui.QColor(100, 10, 10, 40)))
            qp.drawLine(self.begin, self.end)
            self.update()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())
