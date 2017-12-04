from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import language


def setup_tab(num_tab, tab_obj):
    globals()['checkBox'+str(num_tab)] = QtWidgets.QCheckBox(tab_obj)
    globals()['checkBox'+str(num_tab)].setGeometry(QtCore.QRect(460, 20, 17, 21))
    globals()['checkBox'+str(num_tab)].setObjectName('checkBox'+str(num_tab))
    globals()['pushButton'+str(num_tab)] = QtWidgets.QPushButton(tab_obj)
    globals()['pushButton'+str(num_tab)].setGeometry(QtCore.QRect(480, 10, 101, 31))
    globals()['pushButton'+str(num_tab)].setObjectName('pushButton'+str(num_tab))


def fill_tab(ext_dict, tab_obj, start1pos, start2pos):
    globals()['horizontalLayoutWidget'+str(ext_dict['id'])] = QtWidgets.QWidget(tab_obj)
    globals()['horizontalLayoutWidget'+str(ext_dict['id'])].setGeometry(QtCore.QRect(50, start1pos, 600, 41))
    globals()['horizontalLayoutWidget'+str(ext_dict['id'])].setObjectName('horizontalLayoutWidget'+str(ext_dict['id']))
    globals()['horizontalLayout'+str(ext_dict['id'])] = QtWidgets.QHBoxLayout(globals()['horizontalLayoutWidget'+str(ext_dict['id'])])
    globals()['horizontalLayout'+str(ext_dict['id'])].setContentsMargins(0, 0, 0, 0)
    globals()['horizontalLayout'+str(ext_dict['id'])].setObjectName('horizontalLayout'+str(ext_dict['id']))
    globals()['label'+str(ext_dict['id'])] = QtWidgets.QLabel(globals()['horizontalLayoutWidget'+str(ext_dict['id'])])
    globals()['label'+str(ext_dict['id'])].setObjectName('label'+str(ext_dict['id']))
    globals()['label'+str(ext_dict['id'])].setText(ext_dict['name'])
    globals()['horizontalLayout'+str(ext_dict['id'])].addWidget(globals()['label'+str(ext_dict['id'])])
    globals()['label_2'+str(ext_dict['id'])] = QtWidgets.QLabel(globals()['horizontalLayoutWidget'+str(ext_dict['id'])])
    globals()['label_2'+str(ext_dict['id'])].setObjectName('label_2'+str(ext_dict['id']))
    globals()['label_2'+str(ext_dict['id'])].setText(ext_dict['label'])
    globals()['horizontalLayout'+str(ext_dict['id'])].addWidget(globals()['label_2'+str(ext_dict['id'])])
    globals()['ext_menu_button'+str(ext_dict['id'])] = QtWidgets.QMenu()
    """
    menu
    """
    globals()['ext_menu_button'+str(ext_dict['id'])].clear()
    globals()['ext_menu_button'+str(ext_dict['id'])].addAction('PWD')
    globals()['ext_menu_button'+str(ext_dict['id'])].addSeparator()
    globals()['ext_menu_button'+str(ext_dict['id'])].addAction('EMAIL')
    globals()['ext_menu_button'+str(ext_dict['id'])].addSeparator()
    globals()['ext_menu_button'+str(ext_dict['id'])].addAction('WHATEVERWEWANTWEWUDNTW')
    """
    menu end
    """
    globals()['pushButton_5'+str(ext_dict['id'])] = QtWidgets.QPushButton(globals()['horizontalLayoutWidget'+str(ext_dict['id'])])
    globals()['pushButton_5'+str(ext_dict['id'])].setMenu(globals()['ext_menu_button'+str(ext_dict['id'])])
    globals()['pushButton_5'+str(ext_dict['id'])].setObjectName('pushButton_5'+str(ext_dict['id']))
    globals()['horizontalLayout'+str(ext_dict['id'])].addWidget(globals()['pushButton_5'+str(ext_dict['id'])])
    globals()['checkBox2'+str(ext_dict['id'])] = QtWidgets.QCheckBox(globals()['horizontalLayoutWidget'+str(ext_dict['id'])])
    globals()['checkBox2'+str(ext_dict['id'])].setObjectName('checkBox2'+str(ext_dict['id']))
    globals()['checkBox2'+str(ext_dict['id'])].setText(str(ext_dict['id']))
    globals()['horizontalLayout'+str(ext_dict['id'])].addWidget(globals()['checkBox2'+str(ext_dict['id'])])
    globals()['checkBox3'+str(ext_dict['id'])] = QtWidgets.QCheckBox(tab_obj)
    globals()['checkBox3'+str(ext_dict['id'])].setGeometry(QtCore.QRect(20, start2pos, 20, 21))
    globals()['checkBox3'+str(ext_dict['id'])].setObjectName('checkBox3'+str(ext_dict['id']))


def fill_ext(exten_list, tab_obj, exten_widget_start_pos, exten_chkbox_start_pos):
    for ext_dict in exten_list:
        fill_tab(ext_dict, tab_obj, exten_widget_start_pos, exten_chkbox_start_pos)
        exten_widget_start_pos += 40
        exten_chkbox_start_pos += 40


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
        self.ext_menu_window.setObjectName("self.ext_menu_window")
        self.ext_menu_window.resize(607, 600)
        self.pushButton = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 10, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 10, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.ext_menu_window)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 10, 131, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget = QtWidgets.QTabWidget(self.ext_menu_window)
        self.tabWidget.setGeometry(QtCore.QRect(0, 60, 601, 521))
        self.tabWidget.setObjectName("tabWidget")

    def setupUi(self):
        if self.menuform.loginform.token:
            index = 1
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
                setup_tab('page' + str(index), globals()['page' + str(index)])
                exten_widget_start_pos = 70
                exten_chkbox_start_pos = 80
                fill_ext(self.exten_list, globals()['page' + str(index)], exten_widget_start_pos,
                         exten_chkbox_start_pos)
                self.tabWidget.addTab(globals()['page' + str(index)], str(index))
                index += 1
        else:
            self.tabWidget.clear()
            for numbers in self.tubs_num:
                globals()['tab' + str(numbers)] = QtWidgets.QWidget()
                globals()['tab' + str(numbers)].setObjectName('tab' + str(numbers))
                setup_tab('tab' + str(numbers), globals()['tab' + str(numbers)])
                exten_widget_start_pos = 70
                exten_chkbox_start_pos = 80
                fill_ext(self.exten_list, globals()['tab' + str(numbers)], exten_widget_start_pos,
                         exten_chkbox_start_pos)
                self.tabWidget.addTab(globals()['tab' + str(numbers)], str(numbers))
        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.ext_menu_window.setWindowTitle(_translate("self.ext_menu_window", language.ext_dict["ext_menu_window"][self.LANG[0]]))
        self.pushButton.setText(_translate("self.ext_menu_window", "12"))
        self.pushButton_2.setText(_translate("self.ext_menu_window", "9"))
        self.pushButton_3.setText(_translate("self.ext_menu_window", "10"))
        self.pushButton_4.setText(_translate("self.ext_menu_window", "11"))
