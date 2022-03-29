import random

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QFrame, QGridLayout, QPushButton

from customWidgets.games.ticTacToe.ticTacToeCell import TicTacToeCell

style = """
QPushButton {{
    width: 160px;
    height: 160px;
    border-style: solid;
    border-width: 2px;
    border-color: {primary_second_variant};
    background-color: {primary_variant_color};
}}
"""


class TicTacToeBoard(QFrame):
    def __init__(self, parent, theme):
        super(TicTacToeBoard, self).__init__(parent)
        self.layout = QGridLayout()
        self.cells = []
        self.freeCells = []
        self.winner = ""
        self.setupUi(theme)


    def setupUi(self, theme):
        self.setGeometry(QRect(20, 40, 560, 510))
        self.setStyleSheet(style.format(primary_variant_color=theme['primary-variant'],
                                        primary_second_variant=theme['primary-second-variant']))
        for i in range(9):
            self.cells.append(TicTacToeCell(self, i))
            self.cells[i].click_signal.connect(lambda value: self.buttonClick(value))
            self.freeCells.append(i)

        self.layout.addWidget(self.cells[0], 0, 0)
        self.layout.addWidget(self.cells[1], 0, 1)
        self.layout.addWidget(self.cells[2], 0, 2)
        self.layout.addWidget(self.cells[3], 1, 0)
        self.layout.addWidget(self.cells[4], 1, 1)
        self.layout.addWidget(self.cells[5], 1, 2)
        self.layout.addWidget(self.cells[6], 2, 0)
        self.layout.addWidget(self.cells[7], 2, 1)
        self.layout.addWidget(self.cells[8], 2, 2)
        self.setLayout(self.layout)

    def reset(self):
        self.freeCells = []
        self.winner = ""
        for i in range(len(self.cells)):
            self.cells[i].reset()
            self.freeCells.append(i)

    def disable(self):
        for i in range(len(self.cells)):
            self.cells[i].setEnabled(False)

    def buttonClick(self, index):
        self.cells[index].capture("X")
        self.freeCells.remove(index)
        if self.evaluateBoard():
            self.disable()
            print(self.winner)
        elif self.hasFreeCells():
            computerIndex = random.choice(self.freeCells)
            self.cells[computerIndex].capture("O")
            self.freeCells.remove(computerIndex)
        else:
            print("Tie")


    def evaluateBoard(self):
        if self.evaluateCells(self.cells[0], self.cells[1], self.cells[2]) or \
                self.evaluateCells(self.cells[3], self.cells[4], self.cells[5]) or \
                self.evaluateCells(self.cells[6], self.cells[7], self.cells[8]) or \
                self.evaluateCells(self.cells[0], self.cells[3], self.cells[6]) or \
                self.evaluateCells(self.cells[1], self.cells[4], self.cells[7]) or \
                self.evaluateCells(self.cells[2], self.cells[5], self.cells[8]) or \
                self.evaluateCells(self.cells[0], self.cells[4], self.cells[8]) or \
                self.evaluateCells(self.cells[2], self.cells[4], self.cells[6]):
            return True
        return False

    def hasFreeCells(self):
        for cell in self.cells:
            if cell.captured:
                return True
        return False

    def evaluateCells(self, a, b, c):
        if a.captured() and a.text is b.text is c.text:
            if a.text == "X":
                self.winner = "Player win"
            else:
                self.winner = "Computer win"
            return True
        return False
