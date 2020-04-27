# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tuto1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Button1(object):
    def setupUi(self, Button1):
        Button1.setObjectName("Button1")
        Button1.resize(877, 723)
        Button1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Button1.setMouseTracking(False)
        Button1.setTabletTracking(False)
        Button1.setFocusPolicy(QtCore.Qt.WheelFocus)
        Button1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Button1.setDocumentMode(False)
        Button1.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(Button1)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 270, 191, 221))
        self.pushButton.setMinimumSize(QtCore.QSize(5, 0))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton.setObjectName("pushButton")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(150, 20, 231, 191))
        self.label1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label1.setObjectName("label1")
        Button1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Button1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 877, 31))
        self.menubar.setMouseTracking(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Button1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Button1)
        self.statusbar.setObjectName("statusbar")
        Button1.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Button1)
        QtCore.QMetaObject.connectSlotsByName(Button1)

    def retranslateUi(self, Button1):
        _translate = QtCore.QCoreApplication.translate
        Button1.setWindowTitle(_translate("Button1", "MainWindow"))
        self.pushButton.setText(_translate("Button1", "Press Me!"))
        self.label1.setText(_translate("Button1", "Hello my name is Victoria"))
        self.menuFile.setTitle(_translate("Button1", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Button1 = QtWidgets.QMainWindow()
    ui = Ui_Button1()
    ui.setupUi(Button1)
    Button1.show()
    sys.exit(app.exec_())
