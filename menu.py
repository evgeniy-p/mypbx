import language
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class MenuForm:
    def __init__(self):
        self.LANG = 1
        self.menu_window = QMainWindow()
        self.menu_window.move(600, 300)
        self.setupUi(self.menu_window)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(305, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 440, 67, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 430, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 430, 31, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(25, 30, 255, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(25, 70, 255, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(25, 110, 255, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(25, 150, 255, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(25, 190, 255, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(25, 230, 255, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(25, 310, 255, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(25, 270, 255, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 305, 25))
        self.menubar.setObjectName("menubar")
        self.menuHumanpbx = QtWidgets.QMenu(self.menubar)
        self.menuHumanpbx.setObjectName("menuHumanpbx")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHumanpbx.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.menuHumanpbx.setTitle(_translate("MainWindow", language.menu_dict["uptitle"][self.LANG]))

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

