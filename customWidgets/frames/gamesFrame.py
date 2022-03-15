from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QFrame, QVBoxLayout

from customWidgets.frames.focusGamesFrame import FocusGames
from customWidgets.frames.normalGamesFrame import NormalGames
from customWidgets.frames.speakGamesFrame import SpeakGames
from customWidgets.games.ticTacToe.ticTacToe import TicTacToe


class GamesFrame(QFrame):
    def __init__(self, parent, theme):
        super(GamesFrame, self).__init__(parent)
        self.normalGames = NormalGames(self, theme)
        self.speakGames = SpeakGames(self, theme)
        self.focusGames = FocusGames(self, theme)
        self.verticalGamesFrame = QVBoxLayout()
        self.ticTacToeGame = TicTacToe(self, theme)

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(470, 120, 1420, 820))

        # setting layout
        self.verticalGamesFrame.addWidget(self.normalGames)
        self.verticalGamesFrame.addWidget(self.speakGames)
        self.verticalGamesFrame.addWidget(self.focusGames)
        self.setLayout(self.verticalGamesFrame)
