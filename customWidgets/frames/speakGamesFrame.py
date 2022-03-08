from PyQt5.QtWidgets import QFrame


class SpeakGames(QFrame):
    def __init__(self, parent):
        super(SpeakGames, self).__init__(parent)
        self.setStyleSheet("background-color: #31111F")

        self.setupUi()

    def setupUi(self):
        pass
