from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtWidgets, QtCore
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        top = 400
        left = 400
        width = 800
        height = 600

        icon = "icons\paint.png"

        self.setWindowTitle("Paint Application")
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        brushMenu = mainMenu.addMenu("Brush ")
        modeMenu = mainMenu.addMenu("Paint Mode")

        saveAction = QAction(QIcon("icons/save.png"), "Save", self)
        saveAction.setShortcut("Ctrl +S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        BrushSizeAction = QAction(QIcon("icons/size.png"), "Size", self)
        BrushSizeAction.setShortcut("Ctrl + B")
        brushMenu.addAction(BrushSizeAction)
        BrushSizeAction.triggered.connect(self.setBrushSize)

        BrushColorAction = QAction(QIcon("icons/black.png"), "Color", self)
        BrushColorAction.setShortcut("Ctrl + P ")
        brushMenu.addAction(BrushColorAction)
        BrushColorAction.triggered.connect(self.setBrushColor)

        clearAction = QAction(QIcon("icons/clear.png"), "Clear", self)
        clearAction.setShortcut("Ctrl + C ")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

    def setBrushColor(self):
        newColor = QtWidgets.QColorDialog.getColor(self.brushColor)
        if newColor.isValid():
            self.brushColor = newColor

    def setBrushSize(self):
        newSize, success = QtWidgets.QInputDialog.getInt(self, "Scribble", "Select pen width:",
                                                          self.brushSize, 1, 50, 1)
        if success:
            self.brushSize = newSize

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftToolBarArea) & self.drawing:
            position = event.pos()
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, position)
            self.lastPoint = position
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, filter_ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);; JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.node = None
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
