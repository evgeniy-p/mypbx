from PyQt5.QtWidgets import QApplication
import login
import menu
import sys


def run_menu_close_login():
    menu_form.menu_window.show()
    login_form.start_window.close()


def set_ru_lang():
    login_form.LANG = 1
    menu_form.LANG = 1
    login_form.retranslateUi(login_form.start_window)
    menu_form.retranslateUi(menu_form.menu_window)


def set_en_lang():
    login_form.LANG = 0
    menu_form.LANG = 0
    login_form.retranslateUi(login_form.start_window)
    menu_form.retranslateUi(menu_form.menu_window)


app = QApplication(sys.argv)

"""
Инициализация формы логина
"""
login_form = login.LoginForm()
login_form.start_window.show()
"""
Инициализация формы меню
"""
menu_form = menu.MenuForm()
"""
Нажатие кнопок в форме логина 
"""
login_form.pushButton_2.clicked.connect(login_form.login_but_clicked)
login_form.pushButton_2.clicked.connect(run_menu_close_login)
login_form.pushButton_3.clicked.connect(set_ru_lang)
login_form.pushButton_4.clicked.connect(set_en_lang)
"""
Нажатие кнопок в меню 
"""
menu_form.pushButton.clicked.connect(set_en_lang)
menu_form.pushButton_2.clicked.connect(set_ru_lang)
menu_form.pushButton_3.clicked.connect(menu_form.extension_but_clicked)
menu_form.pushButton_4.clicked.connect(menu_form.routing_but_clicked)
menu_form.pushButton_5.clicked.connect(menu_form.cdr_but_clicked)
menu_form.pushButton_6.clicked.connect(menu_form.dialrul_but_clicked)
menu_form.pushButton_7.clicked.connect(menu_form.fax_but_clicked)
"""
Выход
"""
sys.exit(app.exec_())