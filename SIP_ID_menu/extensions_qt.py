from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import language
from SIP_ID_menu import tab_class
from SIP_ID_menu import ext_line


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
        self.menus = ('inccallR', 'record', 'label', 'extnum', 'termpwd', 'oth_sett', 'delete')
        self.tab_dict = dict()
        self.page_dict = dict()
        self.exten_dict = dict()

    def setupUi(self):
        self.page_dict = dict()
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
        # сначала очищаем виджет, чтобы вкладки не дублились
        self.tabWidget.clear()
        while True:
            self.tab_dict = dict()
            self.exten_list = self.menuform.exten_class.get_all_extensions(**{'type': 'phone', 'per_page': '10',
                                                                              'page': str(index)})
            try:
                self.exten_list[0]
            except IndexError:
                return
            # создаем инстанс вкладки - 'tab'
            self.tab_dict[index] = tab_class.Tab(self.LANG)
            # получаем все id добавочных, обративщись к функции, которая заполняет добавочными 'tab'
            self.id_dict[index] = self.fill_tab_ext(index)
            # теперь устанавливаем подменю в кнопку вкладки
            self.tab_dict[index].setup_submenu(self.LANG, index, self.menus)
            # добавляем вкладку на виджет
            self.tabWidget.addTab(self.tab_dict[index].tab_page, str(index))
            index += 1

    def go_demo(self):
        self.tabWidget.clear()
        for tub_numb in self.tubs_nums:
            self.tab_dict[tub_numb] = tab_class.Tab(self.LANG)
            self.fill_tab_ext(tub_numb)
            self.tab_dict[tub_numb].setup_submenu(self.LANG, tub_numb, self.menus)
            self.tabWidget.addTab(self.tab_dict[tub_numb].tab_page, str(tub_numb))

    def fill_tab_ext(self, index):
        id_list = list()
        self.exten_dict = dict()
        exten_widget_start_pos = 70
        exten_chkbox_start_pos = 80
        for ext_dict in self.exten_list:
            self.exten_dict[ext_dict['id']] = ext_line.Extline(self.LANG, self.tab_dict[index].tab_page, ext_dict,
                                                               exten_widget_start_pos, exten_chkbox_start_pos,
                                                               self.menus)
            exten_widget_start_pos += 40
            exten_chkbox_start_pos += 40
            id_list.append(ext_dict['id'])
        self.page_dict[index] = self.exten_dict
        return id_list

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


