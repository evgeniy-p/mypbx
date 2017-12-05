from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import language


class QTExtension:
    def __init__(self, menuform):
        self.menuform = menuform
        self.LANG = self.menuform.LANG
        self.ext_menu_window = QMainWindow()
        self.ext_menu_window.move(650, 300)
        self.ext_menu_window.setFixedWidth(607)
        self.ext_menu_window.setFixedHeight(600)
        self.tubs_num = [1]
        self.exten_list = [{'id': 28, 'name': 'test*123', 'label': 'test'},
                           {'id': 36, 'name': 'test*234', 'label': 'test2'}]
        self.id_dict = {1: [28, 36]}
        self.ext_menu_window.setObjectName("self.ext_menu_window")
        self.ext_menu_window.resize(607, 600)
        self.pushButton = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 180, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 10, 350, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget = QtWidgets.QTabWidget(self.ext_menu_window)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 601, 521))
        self.tabWidget.setObjectName("tabWidget")

    def setupUi(self):
        if self.menuform.loginform.token:
            index = 1
            self.id_dict = dict()
            have_ext = True
            self.tabWidget.clear()
            while have_ext:
                self.exten_list = self.menuform.exten_class.get_all_extensions(**{'type': 'phone', 'per_page': '10',
                                                                                  'page': str(index)})
                try:
                    self.exten_list[0]
                except IndexError:
                    have_ext = False
                    break
                globals()['page' + str(index)] = QtWidgets.QWidget()
                globals()['page' + str(index)].setObjectName('page' + str(index))
                self.setup_tab('page' + str(index), globals()['page' + str(index)])
                exten_widget_start_pos = 70
                exten_chkbox_start_pos = 80
                self.id_dict[index] = self.fill_ext(self.exten_list, globals()['page' + str(index)], exten_widget_start_pos,
                                               exten_chkbox_start_pos)
                self.tabWidget.addTab(globals()['page' + str(index)], str(index))
                index += 1
        else:
            self.tabWidget.clear()
            for numbers in self.tubs_num:
                globals()['tab' + str(numbers)] = QtWidgets.QWidget()
                globals()['tab' + str(numbers)].setObjectName('tab' + str(numbers))
                self.setup_tab('tab' + str(numbers), globals()['tab' + str(numbers)])
                exten_widget_start_pos = 70
                exten_chkbox_start_pos = 80
                self.fill_ext(self.exten_list, globals()['tab' + str(numbers)], exten_widget_start_pos,
                         exten_chkbox_start_pos)
                self.tabWidget.addTab(globals()['tab' + str(numbers)], str(numbers))
        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.ext_menu_window.setWindowTitle(_translate("self.ext_menu_window", language.ext_dict["ext_menu_window"][self.LANG[0]]))
        self.pushButton.setText(_translate("self.ext_menu_window", language.ext_dict["create_ext"][self.LANG[0]]))
        self.pushButton_2.setText(_translate("self.ext_menu_window", language.ext_dict["unused"][self.LANG[0]]))

    def setup_tab(self, num_tab, tab_obj):
        globals()['checkBox' + str(num_tab)] = QtWidgets.QCheckBox(tab_obj)
        globals()['checkBox' + str(num_tab)].setGeometry(QtCore.QRect(505, 20, 17, 21))
        globals()['checkBox' + str(num_tab)].setObjectName('checkBox' + str(num_tab))
        globals()['pushButton' + str(num_tab)] = QtWidgets.QPushButton(tab_obj)
        globals()['pushButton' + str(num_tab)].setGeometry(QtCore.QRect(300, 10, 200, 31))
        globals()['pushButton' + str(num_tab)].setObjectName('pushButton' + str(num_tab))

    def fill_tab(self, ext_dict, tab_obj, start1pos, start2pos):
        globals()['horizontalLayoutWidget' + str(ext_dict['id'])] = QtWidgets.QWidget(tab_obj)
        globals()['horizontalLayoutWidget' + str(ext_dict['id'])].setGeometry(QtCore.QRect(50, start1pos, 600, 41))
        globals()['horizontalLayoutWidget' + str(ext_dict['id'])].setObjectName(
            'horizontalLayoutWidget' + str(ext_dict['id']))
        globals()['horizontalLayout' + str(ext_dict['id'])] = QtWidgets.QHBoxLayout(
            globals()['horizontalLayoutWidget' + str(ext_dict['id'])])
        globals()['horizontalLayout' + str(ext_dict['id'])].setContentsMargins(0, 0, 0, 0)
        globals()['horizontalLayout' + str(ext_dict['id'])].setObjectName('horizontalLayout' + str(ext_dict['id']))
        globals()['label' + str(ext_dict['id'])] = QtWidgets.QLabel(
            globals()['horizontalLayoutWidget' + str(ext_dict['id'])])
        globals()['label' + str(ext_dict['id'])].setObjectName('label' + str(ext_dict['id']))
        globals()['label' + str(ext_dict['id'])].setText(ext_dict['name'])
        globals()['horizontalLayout' + str(ext_dict['id'])].addWidget(globals()['label' + str(ext_dict['id'])])
        globals()['label_2' + str(ext_dict['id'])] = QtWidgets.QLabel(
            globals()['horizontalLayoutWidget' + str(ext_dict['id'])])
        globals()['label_2' + str(ext_dict['id'])].setObjectName('label_2' + str(ext_dict['id']))
        globals()['label_2' + str(ext_dict['id'])].setText(ext_dict['label'])
        globals()['horizontalLayout' + str(ext_dict['id'])].addWidget(globals()['label_2' + str(ext_dict['id'])])
        globals()['ext_menu_button' + str(ext_dict['id'])] = QtWidgets.QMenu()
        """
        extension submenu
        """
        globals()['ext_menu_button' + str(ext_dict['id'])].clear()
        globals()['1st' + str(ext_dict['id'])] = globals()['ext_menu_button' + str(ext_dict['id'])].addAction(
            language.ext_dict["inccallR"][self.LANG[0]])
        globals()['1st' + str(ext_dict['id'])].triggered.connect(
            lambda: self.print_hello_world(ext_dict['id']))
        globals()['ext_menu_button' + str(ext_dict['id'])].addSeparator()
        globals()['2nd' + str(ext_dict['id'])] = globals()['ext_menu_button' + str(ext_dict['id'])].addAction(
            language.ext_dict["record"][self.LANG[0]])
        globals()['2nd' + str(ext_dict['id'])].triggered.connect(
            lambda: self.print_hello_world(ext_dict['id']))
        globals()['ext_menu_button' + str(ext_dict['id'])].addSeparator()
        globals()['3rd' + str(ext_dict['id'])] = globals()['ext_menu_button' + str(ext_dict['id'])].addAction(
            language.ext_dict["label"][self.LANG[0]])
        globals()['3rd' + str(ext_dict['id'])].triggered.connect(
            lambda: self.print_hello_world(ext_dict['id']))
        globals()['4' + str(ext_dict['id'])] = globals()['ext_menu_button' + str(ext_dict['id'])].addAction(
            language.ext_dict["extnum"][self.LANG[0]])
        globals()['4' + str(ext_dict['id'])].triggered.connect(
            lambda: self.print_hello_world(ext_dict['id']))
        globals()['5' + str(ext_dict['id'])] = globals()['ext_menu_button' + str(ext_dict['id'])].addAction(
            language.ext_dict["termpwd"][self.LANG[0]])
        globals()['5' + str(ext_dict['id'])].triggered.connect(
            lambda: self.print_hello_world(ext_dict['id']))
        globals()['6' + str(ext_dict['id'])] = globals()['ext_menu_button' + str(ext_dict['id'])].addAction(
            language.ext_dict["oth_sett"][self.LANG[0]])
        globals()['6' + str(ext_dict['id'])].triggered.connect(
            lambda: self.print_hello_world(ext_dict['id']))
        """
        extension submenu end
        """
        globals()['pushButton_5' + str(ext_dict['id'])] = QtWidgets.QPushButton(
            globals()['horizontalLayoutWidget' + str(ext_dict['id'])])
        globals()['pushButton_5' + str(ext_dict['id'])].setMenu(globals()['ext_menu_button' + str(ext_dict['id'])])
        globals()['pushButton_5' + str(ext_dict['id'])].setObjectName('pushButton_5' + str(ext_dict['id']))
        globals()['horizontalLayout' + str(ext_dict['id'])].addWidget(globals()['pushButton_5' + str(ext_dict['id'])])
        globals()['checkBox2' + str(ext_dict['id'])] = QtWidgets.QCheckBox(
            globals()['horizontalLayoutWidget' + str(ext_dict['id'])])
        globals()['checkBox2' + str(ext_dict['id'])].setObjectName('checkBox2' + str(ext_dict['id']))
        globals()['checkBox2' + str(ext_dict['id'])].setText(str(ext_dict['id']))
        globals()['horizontalLayout' + str(ext_dict['id'])].addWidget(globals()['checkBox2' + str(ext_dict['id'])])
        globals()['checkBox3' + str(ext_dict['id'])] = QtWidgets.QCheckBox(tab_obj)
        globals()['checkBox3' + str(ext_dict['id'])].setGeometry(QtCore.QRect(20, start2pos, 20, 21))
        globals()['checkBox3' + str(ext_dict['id'])].setObjectName('checkBox3' + str(ext_dict['id']))

    def fill_ext(self, exten_list, tab_obj, exten_widget_start_pos, exten_chkbox_start_pos):
        id_list = list()
        for ext_dict in exten_list:
            self.fill_tab(ext_dict, tab_obj, exten_widget_start_pos, exten_chkbox_start_pos)
            exten_widget_start_pos += 40
            exten_chkbox_start_pos += 40
            id_list.append(ext_dict['id'])
        return id_list

    def print_hello_world(self, arg):
        print(str(arg))