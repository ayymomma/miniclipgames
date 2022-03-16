from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QFrame, QHBoxLayout

from customWidgets.games.ticTacToe.TicTacToeFrame import TicTacToeFrame

style = """
QFrame {{
   background-color: {primary_variant_color};
   border-style: solid;
   border-width: 2px;
   border-radius: 10px;
   border-color: {secondary_color};
}}
"""


class NormalGames(QFrame):
    def __init__(self, parent, theme):
        super(NormalGames, self).__init__(parent)

        self.gamesLayout = QHBoxLayout()
        self.ticTacToeFrame = TicTacToeFrame(parent, theme)

        self.setupUi(theme)

    def setupUi(self, theme):
        self.setStyleSheet(style.format(primary_variant_color=theme['primary-variant'],
                                        secondary_color=theme['secondary']))
        self.gamesLayout.setGeometry(QRect(50, 50, 1420, 300))
        self.gamesLayout.addWidget(self.ticTacToeFrame)
        self.setLayout(self.gamesLayout)
