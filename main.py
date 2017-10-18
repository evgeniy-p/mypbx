from PyQt5.QtWidgets import QApplication
import login
import sys


def login_but_clicked():
    print('hello')

def set_RU_lang():
    login_form.LANG = 1
    login_form.retranslateUi(login_form.start_window)

def set_EN_lang():
    login_form.LANG = 0
    login_form.retranslateUi(login_form.start_window)

"""
Инициализация формы логина
"""

app = QApplication(sys.argv)
login_form = login.Login_Form()
login_form.start_window.show()
login_form.pushButton_2.clicked.connect(login_but_clicked)
login_form.pushButton_3.clicked.connect(set_RU_lang)
login_form.pushButton_4.clicked.connect(set_EN_lang)













sys.exit(app.exec_())