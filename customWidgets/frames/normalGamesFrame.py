from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QFrame, QHBoxLayout, QGraphicsBlurEffect

from customWidgets.games.ticTacToe.TicTacToeFrame import TicTacToeFrame

style = """
QFrame {{
   background-color: {primary_variant_color};
   border-radius: 10px;
   border-color: {secondary_color}; 
}}
"""


class NormalGames(QFrame):
    def __init__(self, parent, theme):
        super(NormalGames, self).__init__(parent)

        self.gamesLayout = QHBoxLayout()
        self.ticTacToeFrame = TicTacToeFrame(self, theme)
        self.ticTacToeFrame1 = TicTacToeFrame(self, theme)
        self.ticTacToeFrame2 = TicTacToeFrame(self, theme)
        self.ticTacToeFrame3 = TicTacToeFrame(self, theme)
        self.blur_effect = QGraphicsBlurEffect()

        self.setupUi(theme)

    def setupUi(self, theme):
        self.setStyleSheet(style.format(primary_variant_color=theme['primary-variant'],
                                        secondary_color=theme['secondary']))
        self.blur_effect.setBlurRadius(1.4)
        self.setGraphicsEffect(self.blur_effect)
        self.gamesLayout.setContentsMargins(0, 20, 0, 20)
        self.gamesLayout.setGeometry(QRect(0, 0, self.width(), self.height()))
        self.gamesLayout.addWidget(self.ticTacToeFrame)
        self.gamesLayout.addWidget(self.ticTacToeFrame1)
        self.gamesLayout.addWidget(self.ticTacToeFrame2)
        self.gamesLayout.addWidget(self.ticTacToeFrame3)
        self.setLayout(self.gamesLayout)
