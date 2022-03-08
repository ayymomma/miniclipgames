from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QFrame, QVBoxLayout

from customWidgets.frames.focusGamesFrame import FocusGames
from customWidgets.frames.normalGamesFrame import NormalGames
from customWidgets.frames.speakGamesFrame import SpeakGames


class GamesFrame(QFrame):
    def __init__(self, parent):
        super(GamesFrame, self).__init__(parent)
        self.normalGames = NormalGames(self)
        self.speakGames = SpeakGames(self)
        self.focusGames = FocusGames(self)
        self.verticalGamesFrame = QVBoxLayout()

        self.setupUi()

    def setupUi(self):
        self.setGeometry(QRect(470, 120, 1420, 820))

        # setting layout
        self.verticalGamesFrame.addWidget(self.normalGames)
        self.verticalGamesFrame.addWidget(self.speakGames)
        self.verticalGamesFrame.addWidget(self.focusGames)
        self.setLayout(self.verticalGamesFrame)
