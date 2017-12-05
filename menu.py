import language
import client_info
import extensions
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class MenuForm:
    def __init__(self, loginform):
        self.loginform = loginform
        self.LANG = loginform.LANG
        self.menu_window = QMainWindow()
        self.menu_window.move(300, 300)
        self.menu_window.setFixedWidth(320)
        self.menu_window.setFixedHeight(526)
        self.setupUi(self.menu_window)
        self.start_ext_menu = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(175, 486, 67, 17))
        self.label.setObjectName("label")
        self.label1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 10, 300, 31))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 45, 300, 31))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(10, 80, 300, 31))
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
        MainWindow.setWindowTitle(_translate("MainWindow", language.menu_dict["Menu_WindowTitle"][self.LANG[0]]))
        self.label.setText(_translate("MainWindow", language.menu_dict["languag"][self.LANG[0]]))
        self.pushButton.setText(_translate("MainWindow", "EN"))
        self.pushButton_2.setText(_translate("MainWindow", "RU"))
        self.pushButton_3.setText(_translate("MainWindow", language.menu_dict["Routing"][self.LANG[0]]))
        self.pushButton_4.setText(_translate("MainWindow", language.menu_dict["Extensions"][self.LANG[0]]))
        self.pushButton_5.setText(_translate("MainWindow", language.menu_dict["Queue_Group"][self.LANG[0]]))
        self.pushButton_6.setText(_translate("MainWindow", language.menu_dict["CDR"][self.LANG[0]]))
        self.pushButton_7.setText(_translate("MainWindow", language.menu_dict["conf"][self.LANG[0]]))
        self.pushButton_8.setText(_translate("MainWindow", language.menu_dict["Faxes"][self.LANG[0]]))
        self.pushButton_9.setText(_translate("MainWindow", language.menu_dict["DialRul"][self.LANG[0]]))
        self.pushButton_10.setText(_translate("MainWindow", language.menu_dict["Settings"][self.LANG[0]]))
        self.label1.setText(_translate("MainWindow", language.menu_dict["Hello"][self.LANG[0]]))
        self.passwd = self.setting_menu.addAction(language.menu_dict["passwd"][self.LANG[0]])
        self.setting_menu.addSeparator()
        self.email = self.setting_menu.addAction(language.menu_dict["email"][self.LANG[0]])
        self.setting_menu.addSeparator()
        self.timeZ = self.setting_menu.addAction(language.menu_dict["timeZ"][self.LANG[0]])
        self.setting_menu.addSeparator()
        self.notif = self.setting_menu.addAction(language.menu_dict["notif"][self.LANG[0]])
        self.setting_menu.addSeparator()
        self.wbl = self.setting_menu.addAction(language.menu_dict["white and black list"][self.LANG[0]])
        self.setting_menu.addSeparator()
        self.sounds = self.setting_menu.addAction(language.menu_dict["sounds"][self.LANG[0]])
        """
        В выпадающем списке дергаются необходимые кнопки
        """
        self.passwd.triggered.connect(self.passwd_but_clicked)
        self.email.triggered.connect(self.email_but_clicked)
        self.timeZ.triggered.connect(self.timeZ_but_clicked)
        self.notif.triggered.connect(self.notif_but_clicked)
        self.wbl.triggered.connect(self.wbl_but_clicked)
        self.sounds.triggered.connect(self.sounds_but_clicked)
        if self.loginform.token:
            self.retranslate_user_info()
        else:
            self.label1.setText(_translate("MainWindow", language.menu_dict["Hello"][self.LANG[0]]))
            self.label2.setText(_translate("MainWindow", language.menu_dict["domain"][self.LANG[0]]))
            self.label3.setText(_translate("MainWindow", language.menu_dict["prefix"][self.LANG[0]]))

    def retranslate_user_info(self):
        if self.loginform.token:
            self.clientinfo = client_info.Client(self.loginform)
            _translate = QtCore.QCoreApplication.translate
            self.label1.setText(_translate("MainWindow", language.menu_dict["Hello"][self.LANG[0]] +
                                           self.clientinfo.user_name['name']))
            self.label2.setText(_translate("MainWindow", language.menu_dict["domain"][self.LANG[0]] +
                                           self.clientinfo.clientinfo['domain']))
            self.label3.setText(_translate("MainWindow", language.menu_dict["prefix"][self.LANG[0]] +
                                           self.clientinfo.clientinfo['prefix'] + '*'))
            self.exten_class = extensions.Exten(self)

    def show_demo(self):
        self.menu_window.show()
        self.loginform.start_window.close()

    def routing_but_clicked(self):
        print('routing')

    def extension_but_clicked_show_window(self):
        self.start_ext_menu.show()

    def queue_but_clicked(self):
        print('queue')

    def cdr_but_clicked(self):
        print('cdr')

    def conf_but_clicked(self):
        print('conf')

    def fax_but_clicked(self):
        print('fax')

    def dialrul_but_clicked(self):
        print('dialrul')

    def passwd_but_clicked(self):
        print('passwd')

    def email_but_clicked(self):
        print('email')

    def timeZ_but_clicked(self):
        print('timeZ')

    def notif_but_clicked(self):
        print('notif')

    def wbl_but_clicked(self):
        print('wbl')

    def sounds_but_clicked(self):
        print('sounds')



