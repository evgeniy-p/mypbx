from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow


def setup_tab(num_tab, tab_obj):
    globals()['checkBox{num_tab}'.format(num_tab=num_tab)] = QtWidgets.QCheckBox(tab_obj)
    globals()['checkBox{num_tab}'.format(num_tab=num_tab)].setGeometry(QtCore.QRect(460, 20, 17, 21))
    globals()['checkBox{num_tab}'.format(num_tab=num_tab)].setObjectName('checkBox{num_tab}'.format(num_tab=num_tab))
    globals()['pushButton{num_tab}'.format(num_tab=num_tab)] = QtWidgets.QPushButton(tab_obj)
    globals()['pushButton{num_tab}'.format(num_tab=num_tab)].setGeometry(QtCore.QRect(480, 10, 101, 31))
    globals()['pushButton{num_tab}'.format(num_tab=num_tab)].setObjectName('pushButton{num_tab}'.format(num_tab=num_tab))


def fill_tab(num_tab, tab_obj, start1pos, start2pos):
    globals()['horizontalLayoutWidget{num_tab}'.format(num_tab=num_tab)] = QtWidgets.QWidget(tab_obj)
    globals()['horizontalLayoutWidget{num_tab}'.format(num_tab=num_tab)].setGeometry(QtCore.QRect(50, start1pos, 600, 41))
    globals()['horizontalLayoutWidget{num_tab}'.format(num_tab=num_tab)].setObjectName('horizontalLayoutWidget{num_tab}'.format(num_tab=num_tab))
    globals()['horizontalLayout{num_tab}'.format(num_tab=num_tab)] = QtWidgets.QHBoxLayout(globals()['horizontalLayoutWidget{num_tab}'.format(num_tab=num_tab)])
    globals()['horizontalLayout{num_tab}'.format(num_tab=num_tab)].setContentsMargins(0, 0, 0, 0)
    globals()['horizontalLayout{num_tab}'.format(num_tab=num_tab)].setObjectName('horizontalLayout{num_tab}'.format(num_tab=num_tab))
    globals()['label{num_tab}'.format(num_tab=num_tab)] = QtWidgets.QLabel(globals()['horizontalLayoutWidget{num_tab}'.format(num_tab=num_tab)])
    globals()['label{num_tab}'.format(num_tab=num_tab)].setObjectName('label{num_tab}'.format(num_tab=num_tab))
    globals()['label{num_tab}'.format(num_tab=num_tab)].setText('EXTENSION NAME')
    globals()['horizontalLayout{num_tab}'.format(num_tab=num_tab)].addWidget(globals()['label{num_tab}'.format(num_tab=num_tab)])
    globals()['label_2{num_tab}'.format(num_tab=num_tab)] = QtWidgets.QLabel(globals()['horizontalLayoutWidget{num_tab}'.format(num_tab=num_tab)])
    globals()['label_2{num_tab}'.format(num_tab=num_tab)].setObjectName('label_2{num_tab}'.format(num_tab=num_tab))
    globals()['label_2{num_tab}'.format(num_tab=num_tab)].setText('EXTENSION LABEL')
    globals()['horizontalLayout{num_tab}'.format(num_tab=num_tab)].addWidget(globals()['label_2{num_tab}'.format(num_tab=num_tab)])
    globals()['ext_menu_button{num_tab}'.format(num_tab=num_tab)] = QtWidgets.QMenu()
    """
    menu
    """
    globals()['ext_menu_button{num_tab}'.format(num_tab=num_tab)].clear()
    globals()['ext_menu_button{num_tab}'.format(num_tab=num_tab)].addAction('PWD')
    globals()['ext_menu_button{num_tab}'.format(num_tab=num_tab)].addSeparator()
    globals()['ext_menu_button{num_tab}'.format(num_tab=num_tab)].addAction('EMAIL')
    globals()['ext_menu_button{num_tab}'.format(num_tab=num_tab)].addSeparator()
    globals()['ext_menu_button{num_tab}'.format(num_tab=num_tab)].addAction('WHATEVERWEWANTWEWUDNTW')
    """
    menu end
    """
    globals()['pushButton_5{num_tab}'.format(num_tab=num_tab)] = QtWidgets.QPushButton(globals()['horizontalLayoutWidget{num_tab}'.format(num_tab=num_tab)])
    globals()['pushButton_5{num_tab}'.format(num_tab=num_tab)].setMenu(globals()['ext_menu_button{num_tab}'.format(num_tab=num_tab)])
    globals()['pushButton_5{num_tab}'.format(num_tab=num_tab)].setObjectName('pushButton_5{num_tab}'.format(num_tab=num_tab))
    globals()['horizontalLayout{num_tab}'.format(num_tab=num_tab)].addWidget(globals()['pushButton_5{num_tab}'.format(num_tab=num_tab)])
    globals()['checkBox2{num_tab}'.format(num_tab=num_tab)] = QtWidgets.QCheckBox(globals()['horizontalLayoutWidget{num_tab}'.format(num_tab=num_tab)])
    globals()['checkBox2{num_tab}'.format(num_tab=num_tab)].setObjectName('checkBox2{num_tab}'.format(num_tab=num_tab))
    globals()['checkBox2{num_tab}'.format(num_tab=num_tab)].setText('ID')
    globals()['horizontalLayout{num_tab}'.format(num_tab=num_tab)].addWidget(globals()['checkBox2{num_tab}'.format(num_tab=num_tab)])
    globals()['checkBox3{num_tab}'.format(num_tab=num_tab)] = QtWidgets.QCheckBox(tab_obj)
    globals()['checkBox3{num_tab}'.format(num_tab=num_tab)].setGeometry(QtCore.QRect(20, start2pos, 20, 21))
    globals()['checkBox3{num_tab}'.format(num_tab=num_tab)].setObjectName('checkBox3{num_tab}'.format(num_tab=num_tab))


class QTExtension:
    def __init__(self, classwithtoken):
        self.oldermenu = classwithtoken
        self.LANG = 1
        self.ext_menu_window = QMainWindow()
        self.ext_menu_window.move(650, 300)
        self.ext_menu_window.setFixedWidth(607)
        self.ext_menu_window.setFixedHeight(600)
        self.setupUi(self.ext_menu_window)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 600)
        """
        Кнопки сверху
        """
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 10, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 10, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 10, 131, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 601, 521))
        self.tabWidget.setObjectName("tabWidget")
        """
        Первый таб
        """
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        setup_tab('tab1', self.tab)
        exten_widget_start_pos = 70
        exten_chkbox_start_pos = 80
        exten_list = list(range(10))
        for exten in exten_list:
            print('test', exten_widget_start_pos, exten_chkbox_start_pos)
            fill_tab('tab1' + str(exten), self.tab, exten_widget_start_pos, exten_chkbox_start_pos)
            exten_widget_start_pos += 40
            exten_chkbox_start_pos += 40
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "12"))
        self.pushButton_2.setText(_translate("Form", "9"))
        self.pushButton_3.setText(_translate("Form", "10"))
        self.pushButton_4.setText(_translate("Form", "11"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))

