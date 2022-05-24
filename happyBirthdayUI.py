# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'happyBirthday.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 911)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 541, 61))
        self.lineEdit.setStyleSheet("font-size: 50px;\n"
"background-color: rgb(249, 207, 11);\n"
"color: red;\n"
"border: None;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 90, 61, 61))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: None;\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(61, 61))
        self.pushButton.setObjectName("pushButton")
        self.left = QtWidgets.QLabel(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(20, 159, 111, 741))
        self.left.setStyleSheet("background-color: red;\n"
"font-size: 70px;\n"
"border: 15px solid rgb(249, 207, 11);")
        self.left.setAlignment(QtCore.Qt.AlignCenter)
        self.left.setWordWrap(True)
        self.left.setObjectName("left")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(149, 160, 541, 741))
        self.bg.setStyleSheet("background-color: red;\n"
"border: 10px solid rgb(249, 207, 11);")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.right = QtWidgets.QLabel(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(710, 160, 111, 741))
        self.right.setStyleSheet("background-color: red;\n"
"font-size: 70px;\n"
"border: 15px solid rgb(249, 207, 11);")
        self.right.setAlignment(QtCore.Qt.AlignCenter)
        self.right.setWordWrap(True)
        self.right.setObjectName("right")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(159, 169, 521, 723))
        self.image.setText("")
        self.image.setObjectName("image")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setShortcut(_translate("MainWindow", "Return"))
        self.left.setText(_translate("MainWindow", "天天天真快乐"))
        self.right.setText(_translate("MainWindow", "年年年轻漂亮"))

