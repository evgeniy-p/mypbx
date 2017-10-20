# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import language
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow



class Login_Form:
    def __init__(self):
        self.LANG = 1
        self.start_window = QMainWindow()
        self.start_window.move(500, 500)
        self.setupUi(self.start_window)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 240, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 240, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(140, 200, 150, 22))
        self.checkBox.setObjectName("checkBox")
        self.textBrowser = QtWidgets.QLineEdit(Form)
        self.textBrowser.setGeometry(QtCore.QRect(135, 90, 256, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QLineEdit(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(135, 140, 256, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(12, 100, 130, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(12, 150, 130, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 50, 300, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 0, 31, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 0, 31, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(240, 10, 67, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", language.word_dict["Login_WindowTitle"][self.LANG]))
        self.pushButton.setText(_translate("Form", language.word_dict["show_demo_pushButton"][self.LANG]))
        self.pushButton_2.setText(_translate("Form", language.word_dict["login_button"][self.LANG]))
        self.checkBox.setText(_translate("Form", language.word_dict["read-only"][self.LANG]))
        self.label.setText(_translate("Form", language.word_dict["app ID"][self.LANG]))
        self.label_2.setText(_translate("Form", language.word_dict["app Secret"][self.LANG]))
        self.label_3.setText(_translate("Form", language.word_dict["app credentials"][self.LANG]))
        self.pushButton_3.setText(_translate("Form", language.word_dict["lanru"][self.LANG]))
        self.pushButton_4.setText(_translate("Form", language.word_dict["lanen"][self.LANG]))
        self.label_4.setText(_translate("Form", language.word_dict["languag"][self.LANG]))

