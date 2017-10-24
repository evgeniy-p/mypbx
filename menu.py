import language
import client_info
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class MenuForm:
    def __init__(self, classwithtoken):
        self.classwithtoken = classwithtoken
        self.LANG = 1
        self.menu_window = QMainWindow()
        self.menu_window.move(600, 300)
        self.setupUi(self.menu_window)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 486, 67, 17))
        self.label.setObjectName("label")
        self.label1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 10, 300, 31))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 40, 300, 31))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(10, 70, 300, 31))
        self.label3.setObjectName("label3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 480, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 480, 31, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(28, 165, 268, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(28, 205, 268, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(28, 245, 268, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(28, 285, 268, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(28, 325, 268, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(28, 365, 268, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(28, 405, 268, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(28, 445, 268, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.setting_menu = QtWidgets.QMenu('setting_menu')
        self.pushButton_10.setMenu(self.setting_menu)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setting_menu.clear()
        MainWindow.setWindowTitle(_translate("MainWindow", language.menu_dict["Menu_WindowTitle"][self.LANG]))
        self.label.setText(_translate("MainWindow", language.menu_dict["languag"][self.LANG]))
        self.pushButton.setText(_translate("MainWindow", "EN"))
        self.pushButton_2.setText(_translate("MainWindow", "RU"))
        self.pushButton_3.setText(_translate("MainWindow", language.menu_dict["Extensions"][self.LANG]))
        self.pushButton_4.setText(_translate("MainWindow", language.menu_dict["Routing"][self.LANG]))
        self.pushButton_5.setText(_translate("MainWindow", language.menu_dict["CDR"][self.LANG]))
        self.pushButton_6.setText(_translate("MainWindow", language.menu_dict["DialRul"][self.LANG]))
        self.pushButton_7.setText(_translate("MainWindow", language.menu_dict["Faxes"][self.LANG]))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", language.menu_dict["Settings"][self.LANG]))
        self.label1.setText(_translate("MainWindow", language.menu_dict["Hello"][self.LANG]))
        self.setting_menu.addAction('PWD')
        self.setting_menu.addSeparator()
        self.setting_menu.addAction('EMAIL')
        self.setting_menu.addSeparator()
        self.setting_menu.addAction('WHATEVERWEWANTWEWUDNTWHYSODANGEROUS')

    def extension_but_clicked(self):
        print('Extensions')

    def routing_but_clicked(self):
        print('routing')

    def cdr_but_clicked(self):
        print('cdr')

    def dialrul_but_clicked(self):
        print('dialrul')

    def fax_but_clicked(self):
        print('fax')

    def retranslate_user_info(self):
        if self.classwithtoken.token:
            clientinfo = client_info.Client(self.classwithtoken)
            _translate = QtCore.QCoreApplication.translate
            self.label1.setText(_translate("MainWindow", language.menu_dict["Hello"][self.LANG] +
                                           clientinfo.user_name['name']))
            self.label2.setText(_translate("MainWindow", language.menu_dict["domain"][self.LANG] +
                                           clientinfo.clientinfo['domain']))
            self.label3.setText(_translate("MainWindow", language.menu_dict["prefix"][self.LANG] +
                                           clientinfo.clientinfo['prefix'] + '*'))



