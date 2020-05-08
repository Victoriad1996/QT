
import sys
from PyQt5.QtGui import QPixmap, QColor, QScreen
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
app = QApplication(sys.argv)

w = QWidget()
# img is QImage type
img = QScreen.grabWindow(
        w.winId(),
        x=00,
        y=100,
        width=20,
        height=20,
        ).toImage()

for x in range(0,20):
    for y in range(0,20):
        c = img.pixel(x,y)
        colors = QColor(c).getRgbF()
        print( "(%s,%s) = %s" % (x, y, colors) )
