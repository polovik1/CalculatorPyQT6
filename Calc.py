import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt6.QtCore import QRegularExpression as QRegExp
from PyQt6.QtGui import QRegularExpressionValidator as QRegExpVal
from math import log, sin, cos, tan
from CS10_lib import to10cs, from10cs


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.line = None
        self.display = None
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.line = QLineEdit()
        # self.display.setReadOnly(True)
        regexp = QRegExp('[^a-zA-Zа-яА-Я]')
        self.line.maxLength()
        validator = QRegExpVal(regexp)
        self.line.setValidator(validator)
        self.display = self.line
        grid.addWidget(self.display, 0, 0, 1, 6)
        names = ['1', '2', '3', '+', '/', 'log(',
                 '4', '5', '6', '-', '*', 'sin(',
                 '7', '8', '9', '//', '%', 'cos(',
                 '0', '.', '=', '**', '<', 'tan(',
                 '(', ',', ')', 'to10cs(', 'from10cs(', 'c']

        positions = [(i, j) for i in range(1, 6) for j in range(6)]
        for position, name in zip(positions, names):
            if name == '=':
                btn = QPushButton(name)
                btn.clicked.connect(self.equals)
                grid.addWidget(btn, *position)
            elif name == 'c':
                btn = QPushButton(name)
                btn.clicked.connect(self.clear)
                grid.addWidget(btn, *position)
            elif name == '<':
                btn = QPushButton(name)
                btn.clicked.connect(self.deleteLast)
                grid.addWidget(btn, *position)
            else:
                btn = QPushButton(name)
                btn.clicked.connect(lambda x, b=name: self.append_number(b))
                grid.addWidget(btn, *position)
        self.setLayout(grid)
        self.setWindowTitle('Calculator')

    def append_number(self, b):
        self.display.setText(self.display.text() + b)

    def deleteLast(self):
        self.display.setText(self.display.text()[:-1])

    def clear(self):
        self.display.setText('')

    def equals(self):
        try:
            result = eval(self.display.text())
            result = str(result)
            ogran = 30
            if len(result) > ogran:
                sokr = len(result) - ogran
                result = result[:-sokr]
                result += f'x{sokr}'
            self.display.setText(str(result))
        except:
            try:
                self.display.setText('Error')
            finally:
                self.display.setText('Критическая ошибка')
