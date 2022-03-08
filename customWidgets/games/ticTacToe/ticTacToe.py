from PyQt5 import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton

from customWidgets.games.ticTacToe.ticTacToeBoard import TicTacToeBoard


class TicTacToe(QDialog):
    def __init__(self, parent):
        super(TicTacToe, self).__init__(parent)
        self.board = TicTacToeBoard(self)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Tic Tac Toe")
        self.setMaximumSize(600, 800)
        self.setMinimumSize(600, 800)
        self.show()


