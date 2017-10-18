import PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.login_window = QMainWindow()





if __name__ == '__main__':
    widget = MainWindow()
    widget.run()