from PyQt5.QtWidgets import QApplication
import login
import menu
import sys
import logging


logging.basicConfig(filename='mypbx.log', level=logging.DEBUG)

def set_lang(pref):
    login_form.LANG = pref
    menu_form.LANG = pref
    login_form.retranslateUi(login_form.start_window)
    menu_form.retranslateUi(menu_form.menu_window)
    menu_form.retranslate_user_info()


def set_ru_lang():
    set_lang(1)


def set_en_lang():
    set_lang(0)


app = QApplication(sys.argv)

"""
Инициализация формы логина
"""
login_form = login.LoginForm(logging)
login_form.start_window.show()
"""
Инициализация формы меню
"""
menu_form = menu.MenuForm(login_form)
login_form.start_main_menu = menu_form.menu_window
"""
Нажатие кнопок в форме логина 
"""
login_form.pushButton.clicked.connect(menu_form.show_demo)
login_form.pushButton_2.clicked.connect(login_form.login_but_clicked)
login_form.pushButton_3.clicked.connect(set_ru_lang)
login_form.pushButton_4.clicked.connect(set_en_lang)

"""
Нажатие кнопок в меню 
"""
menu_form.pushButton.clicked.connect(set_en_lang)
menu_form.pushButton_2.clicked.connect(set_ru_lang)
login_form.pushButton_2.clicked.connect(menu_form.retranslate_user_info)
menu_form.pushButton_3.clicked.connect(menu_form.extension_but_clicked)
menu_form.pushButton_4.clicked.connect(menu_form.routing_but_clicked)
menu_form.pushButton_5.clicked.connect(menu_form.cdr_but_clicked)
menu_form.pushButton_6.clicked.connect(menu_form.dialrul_but_clicked)
menu_form.pushButton_7.clicked.connect(menu_form.fax_but_clicked)
"""
Выход
"""
sys.exit(app.exec_())