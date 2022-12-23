from PyQt5 import QtCore, QtGui, QtWidgets
from browse import Ui_MainWindow
import webbrowser
import sys
import requests as req
##

class Browser(QtWidgets.QMainWindow):
    
    def __init__(self):

        super(Browser, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.retranslateUi(self)

        self.history = []

        self.search_system = None

        self.add_function()

    
    def add_function(self):

        
        self.ui.pushButton.clicked.connect(self.search_func)

        self.ui.pushButton_2.clicked.connect(self.show_history)

        self.ui.YandexButton.clicked.connect(lambda: self.set_search_system("Yandex"))

        self.ui.GoogleButton.clicked.connect(lambda: self.set_search_system("Google"))

        self.ui.BingButton.clicked.connect(lambda: self.set_search_system("Bing"))

        self.ui.pushButton_3.clicked.connect(self.open_link)


    def search_func(self):
        
        if self.ui.textEdit.toPlainText():

            if self.search_system == 'Google':

                webbrowser.open(f'https://www.google.com/search?q={self.ui.textEdit.toPlainText()}&rlz=1C1GCEA_enKZ1019KZ1019&oq=.&aqs=chrome..69i57j35i39i362l8.65j0j7&sourceid=chrome&ie=UTF-8')
            
                self.history.append(self.ui.textEdit.toPlainText())

            elif self.search_system == 'Yandex':
                
                webbrowser.open(f'https://yandex.kz/search/?text={self.ui.textEdit.toPlainText()}&lr=10300&search_source=yakz_desktop_common')
            
                self.history.append(self.ui.textEdit.toPlainText())

            elif self.search_system == 'Bing':
                
                webbrowser.open(f'https://www.bing.com/search?q={self.ui.textEdit.toPlainText()}&form=QBLH&sp=-1&pq={self.ui.textEdit.toPlainText()}&sc=5-11&qs=n&sk=&cvid=6D43457462FF4607938FCEA1CADBD16B&ghsh=0&ghacc=0&ghpl=')

                self.history.append(self.ui.textEdit.toPlainText())

            else:

                no_search_system_msg_box = QtWidgets.QMessageBox()

                no_search_system_msg_box.setIcon(QtWidgets.QMessageBox.Warning)

                no_search_system_msg_box.setText("you did not specify a search engine")

                no_search_system_msg_box.setWindowTitle("Search Engine Error")

                no_search_system_msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

                no_search_system_msg_box.exec_()

        else:

            msg_box = QtWidgets.QMessageBox()

            msg_box.setIcon(QtWidgets.QMessageBox.Warning)

            msg_box.setText("Empty search request!")

            msg_box.setWindowTitle("Empty search request error")

            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

            msg_box.setDefaultButton(QtWidgets.QMessageBox.Ok)

            msg_box.exec_()

    def open_link(self) -> None:

        if self.ui.textEdit_2.toPlainText():

            try:

                req.get(self.ui.textEdit_2.toPlainText())

                webbrowser.open(self.ui.textEdit_2.toPlainText())

            except req.exceptions.MissingSchema:

                error_msg_box = QtWidgets.QMessageBox()

                error_msg_box.setIcon(QtWidgets.QMessageBox.Warning)

                error_msg_box.setText('Invalid URL')

                error_msg_box.setWindowTitle("Invalid URL")

                error_msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

                error_msg_box.exec_()

            except req.exceptions.ConnectionError:

                error_msg_box = QtWidgets.QMessageBox()

                error_msg_box.setIcon(QtWidgets.QMessageBox.Warning)

                error_msg_box.setText('Failed to connect')

                error_msg_box.setWindowTitle("Failed to connect")

                error_msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

                error_msg_box.exec_()


    def show_history(self) -> None:

        if self.history:
        
            msg_win = QtWidgets.QMessageBox()

            msg_win.setText('\n\n'.join(self.history))

            msg_win.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

            msg_win.setDefaultButton(QtWidgets.QMessageBox.Ok)

            msg_win.setWindowTitle("History")

            msg_win.setIcon(QtWidgets.QMessageBox.Information)

            msg_win.exec_()

        else:

            msg_win = QtWidgets.QMessageBox()

            msg_win.setText('history is empty')

            msg_win.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

            msg_win.setDefaultButton(QtWidgets.QMessageBox.Ok)

            msg_win.setWindowTitle("History")

            msg_win.setIcon(QtWidgets.QMessageBox.Information)

            msg_win.exec_()

    def set_search_system(self, system: str) -> None:

        self.search_system = system

        self.ui.src_sys_label.setText(system)

def app():

    app = QtWidgets.QApplication(sys.argv)

    window = Browser()

    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    
    app()