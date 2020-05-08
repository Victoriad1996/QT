import numpy as np
import os, sys, locale
from PyQt5 import QtWidgets, QtGui, QtCore


#######################################
# Scribble Area Class
#######################################

class ScribbleArea(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Roots the widget to the top left even if resized
        self.setAttribute(QtCore.Qt.WA_StaticContents)

        # Set defaults for the monitored variables
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        self.myPenColor = QtCore.Qt.blue
        self.myPenMode = "Normal"
        self.myNode = None
        self.mySquare = []
        self.draw = False
        self.Square = True
        self.image = QtGui.QPixmap(200, 200).toImage()

    def setSquare(self):
        self.mySquare = []

    def addSquare(self, point):
        if len(self.mySquare) > 2:
            self.setSquare()
            self.addSquare(point)
        else:
            self.mySquare.append(point)

    def setNode(self, newNode):
        self.myNode = newNode

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def setPenMode(self, newPenMode = "Line"):
        self.myPenMode = newPenMode

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

    # If a mouse button is pressed check if it was the left button and if so store the current position.
    # Set that we are currently drawing
    def mousePressEvent(self, event):
        mode = self.myPenMode
        if event.button() == QtCore.Qt.LeftButton:
            if mode == "Normal":
                self.lastPoint = event.pos()
                self.scribbling = True
            elif mode == "Line":
                print("Line")
                if self.myNode == None:
                    print("No node")
                    self.myNode = event.pos()
                    self.draw = False
                else:
                    print("Node")
                    self.myNode = event.pos()
                    self.drawSimpleLine(event.pos())
                    self.draw = True
            elif mode == "Square":

                size = len(self.mySquare)
                print(size)
                if size==2:
                    self.x = self.mySquare[0].x()
                    self.y = self.mySquare[0].y()
                    self.width = abs(self.mySquare[1].x()-self.mySquare[0].x())
                    self.height = abs(self.mySquare[1].y() - self.mySquare[0].y())
                    self.drawRect(self.x, self.y, self.width, self.height)
                    self.setSquare()
                    self.square = True
                else:
                    print("else")
                    self.addSquare(event.pos())
                    self.square = False


    # When the mouse moves if the left button is clicked we call the drawline function which draws
    # a line from the last position to the current
    def mouseMoveEvent(self, event):
        if ( event.buttons() & QtCore.Qt.LeftButton ) & self.scribbling:
                self.drawLineTo(event.pos())

    # # If the button is released we set variables to stop drawing
    def mouseReleaseEvent(self, event):
        if (event.button() == QtCore.Qt.LeftButton) & self.scribbling & self.myPenMode == "Normal":
            self.drawLineTo(event.pos())
            self.scribbling = False


    # QPainter provides functions to draw on the widget
    # The QPaintEvent is sent to widgets that need to update themselves
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        # Returns the rectangle that needs to be updated
        dirtyRect = event.rect()

        # Draws the rectangle where the image needs to be updated
        painter.drawImage(dirtyRect, self.image, dirtyRect)

    # Resize the image to slightly larger then the main window to cut down on the need to resize the image
    def resizeEvent(self, event):
        if (self.width() > self.image.width()) | (self.height() > self.image.height()):
            newWidth = np.max([self.width() + 128, self.image.width()])
            newHeight = np.max([self.height() + 128, self.image.height()])
            self.resizeImage(self.image, QtCore.QSize(newWidth, newHeight))
            self.update()
        super().resizeEvent(event)

    def drawRect(self, ur,ul, br, bl):
        painter = QtGui.QPainter(self.image)

        # Set the current settings for the pen
        painter.setPen(
            QtGui.QPen(self.myPenColor, self.myPenWidth, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

        painter.drawRect(ur, ul, br, bl)

        self.modified = True

        #rad = (self.myPenWidth // 2) + 2

        # Call to update the rectangular space where we drew
        #self.update(QtCore.QRect(startPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))

    def drawSimpleLine(self, endPoint):

        painter = QtGui.QPainter(self.image)

        # Set the current settings for the pen
        painter.setPen(
            QtGui.QPen(self.myPenColor, self.myPenWidth, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

        # Draw a line from the last registered point to the current
        print("draw simple line", self.myNode, endPoint)
        painter.drawLine(self.myNode, endPoint)

        # Set that the image hasn't been saved
        self.modified = True

        rad = (self.myPenWidth // 2) + 2

        # Call to update the rectangular space where we drew
        self.update(QtCore.QRect(self.myNode, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))

        # Update the last position where we left off drawing
        self.myNode = endPoint

    def drawLineTo(self, endPoint):
        # Used to draw on the widget
        painter = QtGui.QPainter(self.image)

        # Set the current settings for the pen
        painter.setPen(
            QtGui.QPen(self.myPenColor, self.myPenWidth, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

        # Draw a line from the last registered point to the current
        painter.drawLine(self.lastPoint, endPoint)

        # Set that the image hasn't been saved
        self.modified = True

        rad = (self.myPenWidth // 2) + 2

        # Call to update the rectangular space where we drew
        self.update(QtCore.QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))

        # Update the last position where we left off drawing
        self.lastPoint = endPoint

    # When the app is resized create a new image using the changes made to the image
    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        # Create a new image to display and fill it with white
        newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
        newImage.fill(QtGui.qRgb(255, 255, 255))

        # Draw the image
        painter = QtGui.QPainter(newImage)
        painter.drawImage(QtCore.QPoint(0, 0), image)
        self.image = newImage


#######################################
# Main Window Class
#######################################

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the ScribbleArea widget and make it the central widget
        self.scribbleArea = ScribbleArea()
        self.setCentralWidget(self.scribbleArea)

        # Create pen color action and tie to MainWindow::penColor()
        self.penColorAct = QtWidgets.QAction("Pen Color...")
        self.penWidthAct = QtWidgets.QAction("Pen Width...")
        self.penMode = QtWidgets.QAction("Pen Mode...")

        self.clearScreenAct = QtWidgets.QAction("Clear Screen")
        self.clearScreenAct.setShortcut("Ctrl+L")


        self.penColorAct.triggered.connect(self.setPenColor)
        self.penWidthAct.triggered.connect(self.setPenWidth)
        self.clearScreenAct.triggered.connect(self.clearImage)
        self.penMode.triggered.connect(self.setPenMode)

        self.optionMenu = QtWidgets.QMenu("Options")
        self.optionMenu.addAction(self.penColorAct)
        self.optionMenu.addAction(self.penWidthAct)
        self.optionMenu.addAction(self.penMode)
        self.optionMenu.addSeparator()
        self.optionMenu.addAction(self.clearScreenAct)

        # Add menu items to the menubar
        self.menuBar().addMenu(self.optionMenu)


        # Set the title
        self.setWindowTitle("Scribble")

        # Size the app
        self.resize(500, 500)

    def setPenColor(self):
        newColor = QtWidgets.QColorDialog.getColor(self.scribbleArea.myPenColor)
        if newColor.isValid():
            self.scribbleArea.setPenColor(newColor)

    def setPenWidth(self):
        newWidth, success = QtWidgets.QInputDialog.getInt(self, "Scribble", "Select pen width:",
                                                          self.scribbleArea.myPenWidth, 1, 50, 1)
        if success:
            self.scribbleArea.setPenWidth(newWidth)


    def clearImage(self):
        self.scribbleArea.clearImage()

    def setPenMode(self):
        items = ("Normal", "Line", "Square", "Circle")
        item, okPressed = QtWidgets.QInputDialog.getItem(self, "Get item","Mode:", items, 0, False)
        if okPressed and item:
            self.scribbleArea.setPenMode(item)


######################################################
# Start the QT window
######################################################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = MainWindow()
    locale.setlocale(locale.LC_TIME, "en_GB.utf8")
    mainwindow.show()
    sys.exit(app.exec_())
