from PyQt5 import QtCore, QtWidgets
import language


class Tab:
    def __init__(self, LANG):
        self.tab_page = QtWidgets.QWidget()
        self.tab_page.setObjectName('tab_page')
        self.tab_checkBox = QtWidgets.QCheckBox(self.tab_page)
        self.tab_checkBox.setGeometry(QtCore.QRect(505, 20, 17, 21))
        self.tab_checkBox.setObjectName('tab_checkBox')
        self.tab_pushButton = QtWidgets.QPushButton(self.tab_page)
        self.tab_pushButton.setGeometry(QtCore.QRect(language.ext_dict["mass_update_butt"][LANG[0]][0],
                                                     language.ext_dict["mass_update_butt"][LANG[0]][1],
                                                     language.ext_dict["mass_update_butt"][LANG[0]][2],
                                                     language.ext_dict["mass_update_butt"][LANG[0]][3]))
        self.tab_pushButton.setObjectName('tab_pushButton')
        self.tab_pushButton.setText(language.ext_dict["mass_update"][LANG[0]])
        self.tab_setting_menu = QtWidgets.QMenu('tab_setting_menu')
        self.tab_pushButton.setMenu(self.tab_setting_menu )
        self.exten_dict = dict()

    def setup_submenu(self, LANG, tab_attr, menus):
        self.tab_setting_menu.clear()
        for num, submenu in enumerate(menus):
            self.tr_action = self.tab_setting_menu.addAction(language.ext_dict[submenu][LANG[0]])
            self.tr_action.triggered.connect(lambda: self.print_hello_world(tab_attr))
            self.tab_setting_menu.addSeparator()

    def print_hello_world(self, *args):
        print(args)