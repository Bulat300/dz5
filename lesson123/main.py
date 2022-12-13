import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
import datetime

class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.marks = [
            'All right - 5',
            'Good - 4',
            'Bad - 3',
            'Very Bad - 2',
        ]
        self.button = QtWidgets.QPushButton("Get random mark!")
        self.label = QtWidgets.QLabel(
            'Random mark maker',
            alignment=QtCore.Qt.AlignCenter
        )
        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.button_click)

    def button_click(self):
        dt = datetime.datetime.now()
        print(f'Button clicked at {dt}')
        self.label.setText(random.choice(self.marks))

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(1000,800)
    widget.show()

    sys.exit((app.exec()))

