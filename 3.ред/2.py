import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QColorDialog
from PyQt5.QtWidgets import QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Диалоговые окна')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 40)
        self.button_1.setText("Кнопка 1")
        self.button_1.clicked.connect(self.run)

        self.button_2 = QPushButton(self)
        self.button_2.move(50, 70)
        self.button_2.setText("Кнопка 2")
        self.button_2.clicked.connect(self.run)

        self.button_3 = QPushButton(self)
        self.button_3.move(80, 100)
        self.button_3.setText("Кнопка 3")
        self.button_3.clicked.connect(self.run)

        self.button_4 = QPushButton(self)
        self.button_4.move(110, 130)
        self.button_4.setText("Кнопка 4")
        self.button_4.clicked.connect(self.run)

        self.show()

    def run(self):
        current_button = self.sender().text()
        if '1' in current_button:
            color = QColorDialog.getColor()
            print(color)
            if color.isValid():
                self.button_1.setStyleSheet("background-color: {}".format(color.name()))
        elif '2' in current_button:
            i, okBtnPressed = QInputDialog.getItem(self, "Выберите вашу страну",
                                                   "Откуда ты?",
                                                   ("Россия", "Германия", "США"),
                                                   1, False)
            if okBtnPressed:
                self.button_2.setText(i)
        elif '3' in current_button:
            i, okBtnPressed = QInputDialog.getText(self, "Введите имя",
                                                   "Как тебя зовут?")
            if okBtnPressed:
                self.button_3.setText(i)

        elif '4' in current_button:
            i, okBtnPressed = QInputDialog.getInt(self, "Введите возраст",
                                                  "Сколько тебе лет?",
                                                  20, 18, 27, 1)
            if okBtnPressed:
                self.button_4.setText(str(i))

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




