import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QLCDNumber, QLineEdit


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.a = 0

    def initUI(self):
        self.setGeometry(300, 600, 1500, 900)
        self.setWindowTitle('Крестики-нолики')
        self.btn = QPushButton('0', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(0, 0)
        self.btn.resize(300, 300)

        self.btn1 = QPushButton('1', self)
        self.btn1.resize(self.btn.sizeHint())
        self.btn1.move(0, 300)
        self.btn1.resize(300, 300)

        self.btn2 = QPushButton('2', self)
        self.btn2.resize(self.btn.sizeHint())
        self.btn2.move(0, 600)
        self.btn2.resize(300, 300)

        self.btn3 = QPushButton('3', self)
        self.btn3.resize(self.btn.sizeHint())
        self.btn3.move(300, 0)
        self.btn3.resize(300, 300)

        self.btn4 = QPushButton('4', self)
        self.btn4.resize(self.btn.sizeHint())
        self.btn4.move(300, 300)
        self.btn4.resize(300, 300)

        self.btn5 = QPushButton('5', self)
        self.btn5.resize(self.btn.sizeHint())
        self.btn5.move(300, 600)
        self.btn5.resize(300, 300)

        self.btn6 = QPushButton('6', self)
        self.btn6.resize(self.btn.sizeHint())
        self.btn6.move(600, 0)
        self.btn6.resize(300, 300)

        self.btn7 = QPushButton('7', self)
        self.btn7.resize(self.btn.sizeHint())
        self.btn7.move(600, 300)
        self.btn7.resize(300, 300)

        self.btn8 = QPushButton('8', self)
        self.btn8.resize(self.btn.sizeHint())
        self.btn8.move(600, 600)
        self.btn8.resize(300, 300)

        self.label = QLabel(self)
        self.label.setText("Нажимайте на кнопку один раз")
        self.label.move(1100, 100)

        self.btn.clicked.connect(self.b)
        self.btn1.clicked.connect(self.b1)
        self.btn2.clicked.connect(self.b2)
        self.btn3.clicked.connect(self.b3)
        self.btn4.clicked.connect(self.b4)
        self.btn5.clicked.connect(self.b5)
        self.btn6.clicked.connect(self.b6)
        self.btn7.clicked.connect(self.b7)
        self.btn8.clicked.connect(self.b8)

    def b(self):
        self.a += 1
        if self.a % 2 != 0:
            self.btn.setText("{}".format('X'))
            self.btn = 'X'
            if self.btn == 'X' and self.btn1 == 'X' and self.btn2 == 'X' or self.btn == 'X' and self.btn3 == 'X' and \
                    self.btn6 == 'X' or self.btn == 'X' and self.btn4 == 'X' and self.btn8 == 'X':
                self.label.setText("{}".format('ВЫЙГРАЛ X'))

        else:
            self.btn.setText("{}".format('0'))
            self.btn = '0'
            if self.btn == '0' and self.btn1 == '0' and self.btn2 == '0' or self.btn == '0' and self.btn3 == '0' and \
                    self.btn6 == '0' or self.btn == '0' and self.btn4 == '0' and self.btn8 == '0':
                self.label.setText("{}".format('ВЫЙГРАЛ 0'))

    def b1(self):
        self.a += 1
        if self.a % 2 != 0:
            self.btn1.setText("{}".format('X'))
            self.btn1 = 'X'
            if self.btn == 'X' and self.btn1 == 'X' and self.btn2 == 'X' or self.btn1 == 'X' and self.btn4 == 'X' and \
                    self.btn7 == 'X':
                self.label.setText("{}".format('ВЫЙГРАЛ X'))

        else:
            if self.btn == '0' and self.btn1 == '0' and self.btn2 == '0' or self.btn == '0' and self.btn3 == '0' and \
                    self.btn6 == '0':
                self.label.setText("{}".format('ВЫЙГРАЛ 0'))

    def b2(self):
        self.a += 1
        if self.a % 2 != 0:
            self.btn2.setText("{}".format('X'))
            self.btn2 = 'X'
            if self.btn == 'X' and self.btn1 == 'X' and self.btn2 == 'X' or self.btn2 == 'X' and self.btn5 == 'X' and \
                    self.btn8 == 'X' or self.btn2 == 'X' and self.btn4 == 'X' and self.btn6 == 'X':
                self.label.setText("{}".format('ВЫЙГРАЛ X'))

        else:
            self.btn2.setText("{}".format('0'))
            self.btn2 = '0'
            if self.btn == '0' and self.btn1 == '0' and self.btn2 == '0' or self.btn2 == '0' and self.btn5 == '0' and \
                    self.btn8 == '0' or self.btn2 == '0' and self.btn4 == '0' and self.btn6 == '0':
                self.label.setText("{}".format('ВЫЙГРАЛ 0'))

    def b3(self):
        self.a += 1
        if self.a % 2 != 0:
            self.btn3.setText("{}".format('X'))
            self.btn3 = 'X'
            if self.btn == 'X' and self.btn3 == 'X' and self.btn6 == 'X' or self.btn3 == 'X' and self.btn4 == 'X' and \
                    self.btn5 == 'X':
                self.label.setText("{}".format('ВЫЙГРАЛ X'))

        else:
            self.btn3.setText("{}".format('0'))
            self.btn3 = '0'
            if self.btn == '0' and self.btn3 == '0' and self.btn6 == '0' or self.btn3 == '0' and self.btn4 == '0' and \
                    self.btn5 == '0':
                self.label.setText("{}".format('ВЫЙГРАЛ 0'))

    def b4(self):
        self.a += 1
        if self.a % 2 != 0:
            self.btn4.setText("{}".format('X'))
            self.btn4 = 'X'
            if self.btn1 == 'X' and self.btn4 == 'X' and self.btn7 == 'X' or self.btn3 == 'X' and self.btn4 == 'X' and \
                    self.btn5 == 'X':
                self.label.setText("{}".format('ВЫЙГРАЛ X'))

        else:
            self.btn4.setText("{}".format('0'))
            self.btn4 = '0'
            if self.btn1 == '0' and self.btn4 == '0' and self.btn7 == '0' or self.btn3 == '0' and self.btn4 == '0' and \
                    self.btn5 == '0':
                self.label.setText("{}".format('ВЫЙГРАЛ 0'))

    def b5(self):
        self.a += 1
        if self.a % 2 != 0:
            self.btn5.setText("{}".format('X'))
            self.btn5 = 'X'
            if self.btn2 == 'X' and self.btn5 == 'X' and self.btn8 == 'X' or self.btn3 == 'X' and self.btn4 == 'X' and \
                    self.btn5 == 'X':
                self.label.setText("{}".format('ВЫЙГРАЛ X'))

        else:
            self.btn5.setText("{}".format('0'))
            self.btn5 = '0'
            if self.btn2 == '0' and self.btn5 == '0' and self.btn8 == '0' or self.btn3 == '0' and self.btn4 == '0' and \
                    self.btn5 == '0':
                self.label.setText("{}".format('ВЫЙГРАЛ 0'))

    def b6(self):
        self.a += 1
        if self.a % 2 != 0:
            self.btn6.setText("{}".format('X'))
            self.btn6 = 'X'
            if self.btn6 == 'X' and self.btn7 == 'X' and self.btn8 == 'X' or self.btn == 'X' and self.btn3 == 'X' and \
                    self.btn6 == 'X' or self.btn6 == 'X' and self.btn4 == 'X' and self.btn2 == 'X':
                self.label.setText("{}".format('ВЫЙГРАЛ X'))

        else:
            self.btn6.setText("{}".format('0'))
            self.btn6 = '0'
            if self.btn6 == '0' and self.btn7 == '0' and self.btn8 == '0' or self.btn == '0' and self.btn3 == '0' and \
                    self.btn6 == '0' or self.btn6 == '0' and self.btn4 == '0' and self.btn2 == '0':
                self.label.setText("{}".format('ВЫЙГРАЛ 0'))

    def b7(self):
        self.a += 1
        if self.a % 2 != 0:
            self.btn7.setText("{}".format('X'))
            self.btn7 = 'X'
            if self.btn6 == 'X' and self.btn7 == 'X' and self.btn8 == 'X' or self.btn1 == 'X' and self.btn4 == 'X' and \
                    self.btn7 == 'X':
                self.label.setText("{}".format('ВЫЙГРАЛ X'))

        else:
            self.btn7.setText("{}".format('0'))
            self.btn7 = '0'
            if self.btn6 == '0' and self.btn7 == '0' and self.btn8 == '0' or self.btn1 == '0' and self.btn4 == '0' and \
                    self.btn7 == '0':
                self.label.setText("{}".format('ВЫЙГРАЛ 0'))

    def b8(self):
        self.a += 1
        if self.a % 2 != 0:
            self.btn8.setText("{}".format('X'))
            self.btn8 = 'X'
            if self.btn8 == 'X' and self.btn7 == 'X' and self.btn6 == 'X' or self.btn2 == 'X' and self.btn5 == 'X' and \
                    self.btn8 == 'X' or self.btn == 'X' and self.btn4 == 'X' and self.btn8 == 'X':
                self.label.setText("{}".format('ВЫЙГРАЛ X'))


        else:
            self.btn8.setText("{}".format('0'))
            self.btn8 = '0'
            if self.btn8 == '0' and self.btn7 == '0' and self.btn6 == '0' or self.btn2 == '0' and self.btn5 == '0' and \
                    self.btn8 == '0' or self.btn == '0' and self.btn4 == '0' and self.btn8 == '0':
                self.label.setText("{}".format('ВЫЙГРАЛ 0'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())