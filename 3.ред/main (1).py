import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from main_win_re import Ui_MainWindow


class TextReader(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.filename = ('exexex.txt')
        self.pushButton.clicked.connect(self.load_text_file)
        self.pushButton_save.clicked.connect(self.save_text)
        self.pushButton_save_as.clicked.connect(self.save_as_text_file)
        self.textBrowser.textChanged.connect(self.dynamic_title)

    def load_text_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')[0]
        self.filename = filename
        try:
            with open(filename, 'r') as input_file:
                data = input_file.read()
            self.textBrowser.setText(data)
            self.setWindowTitle(filename)
        except FileNotFoundError as e:
            print(e)
            self.show_dialog(e)

    def save_text(self):
        text = self.textBrowser.toPlainText()
        print(text)
        try:
            with open(self.filename, 'w') as output_file:
                output_file.write(text)
                filename = self.filename
                self.setWindowTitle(filename)
        except Exception as e:
            self.show_dialog(e)

    def save_as_text_file(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')[0]
        text = self.textBrowser.toPlainText()
        try:
            with open(filename, 'w') as output_file:
                output_file.write(text)
            self.setWindowTitle(filename)
            self.filename = filename
        except Exception as e:
            self.show_dialog(e)

    def dynamic_title(self):
        self.setWindowTitle(self.filename + '*')

    def show_dialog(self, excep):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText('Unexpected error.')
        msg.setInformativeText(str(excep))
        msg.setWindowTitle('Exception')
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg.exec_()
        if retval == QMessageBox.Ok:
            print('Ok')
        else:
            print('Cancel')
        print('value of pressed message box button: ', retval)



sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextReader()
    ex.show()
    sys.exit(app.exec())
