import sys
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QColorDialog

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pass

    def run(self):
        i, okBtnPressed - QInputDialog.getText(self, 'Vvedite vozrast, "Skolko let?')
        print(i, okBtnPressed)
        if okBtnPressed:
            self.button_1.setText(i)

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())