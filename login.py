import language
import myexception
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import gettoken


class LoginForm(gettoken.Token):
    def __init__(self, log):
        gettoken.Token.__init__(self)
        self.log = log
        self.LANG = 1
        self.start_window = QMainWindow()
        self.start_window.move(300, 300)
        self.start_window.setFixedWidth(400)
        self.start_window.setFixedHeight(300)
        self.setupUi(self.start_window)
        self.start_main_menu = None


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(200, 240, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 240, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QLineEdit(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 90, 256, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QLineEdit(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(100, 140, 256, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 100, 80, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 80, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(80, 50, 300, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 10, 32, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 10, 32, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(240, 15, 50, 17))
        self.label_4.setObjectName("label_4")
        self.errormessage = QtWidgets.QMessageBox()
        self.errormessage.setGeometry(QtCore.QRect(400, 600, 305, 25))
        self.errormessage.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.errormessage.setDefaultButton(QtWidgets.QMessageBox.Ok)
        self.errormessage.setEscapeButton(QtWidgets.QMessageBox.Ok)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", language.login_dict["Login_WindowTitle"][self.LANG]))
        self.pushButton.setText(_translate("Form", language.login_dict["show_demo_pushButton"][self.LANG]))
        self.pushButton_2.setText(_translate("Form", language.login_dict["login_button"][self.LANG]))
        self.label.setText(_translate("Form", language.login_dict["app ID"][self.LANG]))
        self.label_2.setText(_translate("Form", language.login_dict["app Secret"][self.LANG]))
        self.label_3.setText(_translate("Form", language.login_dict["app credentials"][self.LANG]))
        self.pushButton_3.setText(_translate("Form", "RU"))
        self.pushButton_4.setText(_translate("Form", "EN"))
        self.label_4.setText(_translate("Form", language.login_dict["languag"][self.LANG]))
        self.errormessage.setWindowTitle(language.login_dict["error frame name"][self.LANG])

    def login_but_clicked(self):
        try:
            self.get_token(self.textBrowser.text(), self.textBrowser_2.text())
        except myexception.cant_get_OK_check_login_and_password:
            self.log.warning("cant_get_OK_check_login_and_password")
            self.errormessage.setText(language.login_dict['login warning'][self.LANG])
            self.errormessage.setDetailedText(language.login_dict["app credentials wrong"][self.LANG])
            self.errormessage.show()
        else:
            self.start_main_menu.show()
            self.start_window.close()
