from PyQt5 import Qt, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton

from customWidgets.games.ticTacToe.ticTacToeBoard import TicTacToeBoard

style = """
QDialog {{
    background-color: {primary_color};
}}
"""


class TicTacToe(QDialog):
    def __init__(self, parent, theme):
        super(TicTacToe, self).__init__(parent)
        self.board = TicTacToeBoard(self, theme)
        self.setupUi(theme)

    def setupUi(self, theme):
        self.setWindowTitle("Tic Tac Toe")
        self.setMaximumSize(600, 800)
        self.setMinimumSize(600, 800)
        self.setStyleSheet(style.format(primary_color=theme['primary']))
        self.show()

