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
        self.ext_menu_window.setFixedHeight(650)
        self.tubs_nums = [1]
        self.exten_list = [{'id': 28, 'name': 'test*123', 'label': 'test'},
                           {'id': 36, 'name': 'test*234', 'label': 'test2'}]
        self.id_dict = {1: [28, 36]}
        self.ext_menu_window.setObjectName("self.ext_menu_window")
        self.ext_menu_window.resize(607, 600)
        self.pushButton = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton.setGeometry(QtCore.QRect(5, 10, 180, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 10, 300, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton_3.setGeometry(QtCore.QRect(495, 10, 105, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton_4.setGeometry(QtCore.QRect(5, 600, 295, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton_5.setGeometry(QtCore.QRect(305, 600, 300, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget = QtWidgets.QTabWidget(self.ext_menu_window)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 601, 521))
        self.tabWidget.setObjectName("tabWidget")

    def setupUi(self):
        if self.menuform.loginform.token:
            self.set_extensions()
        else:
            self.go_demo()
        self.ext_menu_window.setWindowTitle(language.ext_dict["ext_menu_window"][self.LANG[0]])
        self.pushButton.setText(language.ext_dict["create_ext"][self.LANG[0]])
        self.pushButton_2.setText(language.ext_dict["unused"][self.LANG[0]])
        self.pushButton_3.setText(language.ext_dict["refresh_but"][self.LANG[0]])
        self.pushButton_4.setText(language.ext_dict["all_this_page"][self.LANG[0]])
        self.pushButton_5.setText(language.ext_dict["all_all_page"][self.LANG[0]])
        self.check_box_set_unset()

    def set_extensions(self):
        index = 1
        self.id_dict = dict()
        self.tabWidget.clear()
        while True:
            self.exten_list = self.menuform.exten_class.get_all_extensions(**{'type': 'phone', 'per_page': '10',
                                                                              'page': str(index)})
            try:
                self.exten_list[0]
            except IndexError:
                return
            globals()['page' + str(index)] = QtWidgets.QWidget()
            globals()['page' + str(index)].setObjectName('page' + str(index))
            self.setup_tab('page' + str(index), globals()['page' + str(index)])
            self.id_dict[index] = self.fill_tab_ext(self.exten_list, globals()['page' + str(index)], 70, 80)
            self.tabWidget.addTab(globals()['page' + str(index)], str(index))
            index += 1

    def go_demo(self):
        self.tabWidget.clear()
        for tub_numb in self.tubs_nums:
            globals()['tab' + str(tub_numb)] = QtWidgets.QWidget()
            globals()['tab' + str(tub_numb)].setObjectName('tab' + str(tub_numb))
            self.setup_tab('page' + str(tub_numb), globals()['tab' + str(tub_numb)])
            self.fill_tab_ext(self.exten_list, globals()['tab' + str(tub_numb)], 70, 80)
            self.tabWidget.addTab(globals()['tab' + str(tub_numb)], str(tub_numb))

    def setup_tab(self, num_tab, tab_obj):
        globals()['checkBox' + str(num_tab)] = QtWidgets.QCheckBox(tab_obj)
        globals()['checkBox' + str(num_tab)].setGeometry(QtCore.QRect(505, 20, 17, 21))
        globals()['checkBox' + str(num_tab)].setObjectName('checkBox' + str(num_tab))
        globals()['pushButton' + str(num_tab)] = QtWidgets.QPushButton(tab_obj)
        globals()['pushButton' + str(num_tab)].setGeometry(QtCore.QRect(language.ext_dict["mass_update_butt"][self.LANG[0]][0],
                                                                        language.ext_dict["mass_update_butt"][self.LANG[0]][1],
                                                                        language.ext_dict["mass_update_butt"][self.LANG[0]][2],
                                                                        language.ext_dict["mass_update_butt"][self.LANG[0]][3]))
        globals()['pushButton' + str(num_tab)].setObjectName('pushButton' + str(num_tab))
        globals()['pushButton' + str(num_tab)].setText(language.ext_dict["mass_update"][self.LANG[0]])
        globals()['setting_menu' + str(num_tab)] = QtWidgets.QMenu('setting_menu' + str(num_tab))
        globals()['pushButton' + str(num_tab)].setMenu(globals()['setting_menu' + str(num_tab)])
        self.setup_submenu(True, 'setting_menu', num_tab, 'inccallR', 'record', 'label', 'extnum',
                           'termpwd', 'oth_sett', 'delete')

    def fill_tab_ext(self, exten_list, tab_obj, exten_widget_start_pos, exten_chkbox_start_pos):
        id_list = list()
        for ext_dict in exten_list:
            self.fill_ext_line(ext_dict, tab_obj, exten_widget_start_pos, exten_chkbox_start_pos)
            exten_widget_start_pos += 40
            exten_chkbox_start_pos += 40
            id_list.append(ext_dict['id'])
        return id_list

    def fill_ext_line(self, ext_dict, tab_obj, start1pos, start2pos):
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
        self.setup_submenu(None, 'ext_menu_button', ext_dict['id'], 'inccallR', 'record', 'label',
                           'extnum', 'termpwd', 'oth_sett', 'delete')
        globals()['pushButton_5' + str(ext_dict['id'])] = QtWidgets.QPushButton(
            globals()['horizontalLayoutWidget' + str(ext_dict['id'])])
        globals()['pushButton_5' + str(ext_dict['id'])].setMenu(globals()['ext_menu_button' + str(ext_dict['id'])])
        globals()['pushButton_5' + str(ext_dict['id'])].setObjectName('pushButton_5' + str(ext_dict['id']))
        globals()['pushButton_5' + str(ext_dict['id'])].setText(language.ext_dict["ext_butt"][self.LANG[0]])
        globals()['horizontalLayout' + str(ext_dict['id'])].addWidget(globals()['pushButton_5' + str(ext_dict['id'])])
        globals()['checkBox2' + str(ext_dict['id'])] = QtWidgets.QCheckBox(
            globals()['horizontalLayoutWidget' + str(ext_dict['id'])])
        globals()['checkBox2' + str(ext_dict['id'])].setObjectName('checkBox2' + str(ext_dict['id']))
        globals()['checkBox2' + str(ext_dict['id'])].setText(str(ext_dict['id']))
        globals()['horizontalLayout' + str(ext_dict['id'])].addWidget(globals()['checkBox2' + str(ext_dict['id'])])
        globals()['checkBox3' + str(ext_dict['id'])] = QtWidgets.QCheckBox(tab_obj)
        globals()['checkBox3' + str(ext_dict['id'])].setGeometry(QtCore.QRect(20, start2pos, 20, 21))
        globals()['checkBox3' + str(ext_dict['id'])].setObjectName('checkBox3' + str(ext_dict['id']))

    def setup_submenu(self, on_page, name, ext_id, *args):
        if on_page:
            ATTR = self.get_page_checkbox()
        else:
            ATTR = ext_id
        globals()[name + str(ext_id)].clear()
        for num, submenu in enumerate(args):
            globals()[str(num) + str(ext_id)] = globals()[name + str(ext_id)].addAction(language.ext_dict[submenu]
                                                                                             [self.LANG[0]])
            globals()[str(num) + str(ext_id)].triggered.connect(lambda: self.print_hello_world(ATTR))
            globals()[name + str(ext_id)].addSeparator()

    def get_page_checkbox(self):
        return 'test'

    def check_box_stat(self):
        pass

    def check_box_set_unset(self):
        pass

    def print_hello_world(self, *args):
        print(str(*args))

    def print_all_ids(self):
        print(self.id_dict)
    

