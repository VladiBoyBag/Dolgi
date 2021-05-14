import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QErrorMessage, QFileDialog, QLabel
from PyQt5.QtGui import QPixmap

SCREEN_SIZE = [1500, 1500]


class ShowPic(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI(self)

    def initUI(self):
        self.setGeometry(400, 400, * SCREEN_SIZE)
        self.setWindowTitle('Why are you looking here?')

        self.pixmap('134.png')
        self.image = QLabel(self)
        self.image.move(80, 60)
        self.image.resize(250, 250)
        self.image.setPixmap(self.pixmap)



sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ShowPic()
    ex.show()
    sys.exit(app.exec())