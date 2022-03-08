from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QFrame, QGridLayout, QPushButton

from customWidgets.games.ticTacToe.ticTacToeCell import TicTacToeCell

style = """
QPushButton {
    width: 160px;
    height: 160px;
    border-style: solid;
    border-width: 2px;
    border-color: #606368;
    background-color: #30363F;
}
"""


class TicTacToeBoard(QFrame):
    def __init__(self, parent):
        super(TicTacToeBoard, self).__init__(parent)
        self.layout = QGridLayout()
        self.cells = []
        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(20, 40, 560, 510))
        self.setStyleSheet(style)
        [self.cells.append(TicTacToeCell(self)) for i in range(9)]
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
        for cell in self.cells:
            cell.reset()

    def disable(self):
        for cell in self.cells:
            cell.setEnable(False)