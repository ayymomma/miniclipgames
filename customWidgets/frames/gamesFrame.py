from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtWidgets import QFrame, QVBoxLayout

from customWidgets.frames.focusGamesFrame import FocusGames
from customWidgets.frames.normalGamesFrame import NormalGames
from customWidgets.frames.speakGamesFrame import SpeakGames
from customWidgets.games.ticTacToe.ticTacToe import TicTacToe


class GamesFrame(QFrame):
    onGameClick_signal = pyqtSignal()

    def __init__(self, parent, theme):
        super(GamesFrame, self).__init__(parent)
        self.normalGames = NormalGames(self, theme)
        self.speakGames = SpeakGames(self, theme)
        self.focusGames = FocusGames(self, theme)
        self.verticalGamesFrame = QVBoxLayout()
        # self.ticTacToeGame = TicTacToe(self, theme)

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(470, 40, 1420, 1000))
        self.normalGames.onTicTacToeClick_signal.connect(lambda: self.onGameClick())

        # setting layout
        self.verticalGamesFrame.setSpacing(10)
        self.verticalGamesFrame.addWidget(self.normalGames)
        self.verticalGamesFrame.addWidget(self.speakGames)
        self.verticalGamesFrame.addWidget(self.focusGames)
        self.setLayout(self.verticalGamesFrame)

    def onGameClick(self):
        self.onGameClick_signal.emit()
