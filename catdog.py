# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catdog.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(-350, -60, 1191, 731))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("dog.jpg"))
        self.photo.setScaledContents(False)
        self.photo.setObjectName("photo")
        self.cat = QtWidgets.QPushButton(self.centralwidget)
        self.cat.setGeometry(QtCore.QRect(30, 640, 331, 31))
        self.cat.setObjectName("cat")
        self.dog = QtWidgets.QPushButton(self.centralwidget)
        self.dog.setGeometry(QtCore.QRect(470, 630, 341, 41))
        self.dog.setObjectName("dog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.cat.clicked.connect(self.show_cat)
        self.dog.clicked.connect(self.show_dog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cat.setText(_translate("MainWindow", "CAT"))
        self.dog.setText(_translate("MainWindow", "DOG"))

    def show_dog(self):

        self.photo.setGeometry(QtCore.QRect(-350, -60, 1191, 731))
        self.photo.setPixmap(QtGui.QPixmap("dog.jpg"))
    def show_cat(self):

        self.photo.setGeometry(QtCore.QRect(100, 0, 1191, 731))
        self.photo.setPixmap(QtGui.QPixmap("cat.jpg"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
