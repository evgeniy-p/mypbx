from PyQt5.QtWidgets import QApplication
import login
import gettoken
import myexception
import sys


def login_but_clicked():
    program_token = gettoken.Token(login_form.textBrowser.text(), login_form.textBrowser_2.text())
    try:
        print(program_token.get_token())
    except myexception.cant_get_OK_check_appid_and_secret:
        print('not ok. bro')
    print(login_form.checkBox.checkState())


def set_ru_lang():
    login_form.LANG = 1
    login_form.retranslateUi(login_form.start_window)


def set_en_lang():
    login_form.LANG = 0
    login_form.retranslateUi(login_form.start_window)

"""
Инициализация формы логина
"""

app = QApplication(sys.argv)
login_form = login.Login_Form()
login_form.start_window.show()

"""
Нажатия кнопок в форме логина 
"""
login_form.pushButton_2.clicked.connect(login_but_clicked)
login_form.pushButton_3.clicked.connect(set_ru_lang)
login_form.pushButton_4.clicked.connect(set_en_lang)













sys.exit(app.exec_())