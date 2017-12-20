from PyQt5 import QtCore, QtWidgets
import language


class Extline:
    def __init__(self, older_menu, tab_obj, ext_dict, start1pos, start2pos):
        self.older_menu = older_menu
        self.ext_horizontalLayoutWidget = QtWidgets.QWidget(tab_obj)
        self.ext_horizontalLayoutWidget.setGeometry(QtCore.QRect(50, start1pos, 600, 41))
        self.ext_horizontalLayoutWidget.setObjectName('ext_horizontalLayoutWidget')
        self.ext_horizontalLayout = QtWidgets.QHBoxLayout(self.ext_horizontalLayoutWidget)
        self.ext_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ext_horizontalLayout.setObjectName('ext_horizontalLayout')
        self.ext_label = QtWidgets.QLabel(self.ext_horizontalLayoutWidget)
        self.ext_label.setObjectName('ext_label')
        self.ext_label.setText(ext_dict['name'])
        self.ext_label.setToolTip(language.ext_dict["info_sip_id_start"][self.older_menu.LANG[0]] + '\n\n' +
                                  language.ext_dict["login"][self.older_menu.LANG[0]] + ext_dict['name'] + '\n' +
                                  language.ext_dict["domain"][self.older_menu.LANG[0]] + ext_dict['domain'] + '\n\n' +
                                  language.ext_dict["info_sip_id_end"][self.older_menu.LANG[0]])
        self.ext_horizontalLayout.addWidget(self.ext_label)
        self.ext_label_2 = QtWidgets.QLabel(self.ext_horizontalLayoutWidget)
        self.ext_label_2.setObjectName('ext_label_2')
        self.ext_label_2.setText(self.make_normal_label(ext_dict['label']))
        self.ext_label_2.setToolTip(ext_dict['label'])
        self.ext_horizontalLayout.addWidget(self.ext_label_2)
        self.ext_menu_button = QtWidgets.QMenu()
        self.ext_pushButton_5 = QtWidgets.QPushButton(self.ext_horizontalLayoutWidget)
        self.ext_pushButton_5.setMenu(self.ext_menu_button)
        self.ext_pushButton_5.setObjectName('ext_pushButton_5')
        self.ext_pushButton_5.setText(language.ext_dict["ext_butt"][self.older_menu.LANG[0]])
        self.setup_submenu(ext_dict['id'])
        self.ext_horizontalLayout.addWidget(self.ext_pushButton_5)
        self.ext_checkBox2 = QtWidgets.QCheckBox(self.ext_horizontalLayoutWidget)
        self.ext_checkBox2.setObjectName('checkBox2' + str(ext_dict['id']))
        self.ext_checkBox2.setText(str(ext_dict['id']))
        self.ext_horizontalLayout.addWidget(self.ext_checkBox2)
        self.ext_checkBox3 = QtWidgets.QCheckBox(tab_obj)
        self.ext_checkBox3.setGeometry(QtCore.QRect(20, start2pos, 20, 21))
        self.ext_checkBox3.setObjectName('ext_checkBox3')

    def setup_submenu(self, ext_id):
        self.ext_menu_button.clear()
        for num, submenu in enumerate(self.older_menu.menus):
            self.tr_action = self.ext_menu_button.addAction(language.ext_dict[submenu][self.older_menu.LANG[0]])
            self.tr_action.triggered.connect(lambda: self.older_menu.print_tmst(ext_id))
            self.ext_menu_button.addSeparator()

    def make_normal_label(self, name):
        if name:
            if len(name) > 16:
                name = name[:16] + '...'
        return name