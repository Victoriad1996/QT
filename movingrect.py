import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QRect, QPoint

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle('Colours')
        self.btnPaint = QPushButton("Paint", self)
        self.btnMove = QPushButton("Move x+1 y+1", self)
        self.rect = QRect()

        self.btnPaint.clicked.connect(self.onPaint)
        self.btnMove.clicked.connect(self.onMove)

        self.hlayout = QHBoxLayout(self)
        self.hlayout.addWidget(self.btnPaint)
        self.hlayout.addWidget(self.btnMove)
        self.hlayout.addStretch(1)
        self.show()

    def onPaint(self):
        if self.rect.isNull():
            self.rect = QRect(10, 15, 80, 45)
            self.update()

    def onMove(self):
        if not self.rect.isNull():
            self.rect.translate(QPoint(1, 1))
            self.update()

    def paintEvent(self, e):
        qp = QPainter(self)
        qp.setPen(QColor("#d4d4d4"))
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(self.rect)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
