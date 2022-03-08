from PyQt5.QtWidgets import QFrame


class NormalGames(QFrame):
    def __init__(self, parent):
        super(NormalGames, self).__init__(parent)
        self.setStyleSheet("background-color: #30363F")

        self.setupUi()

    def setupUi(self):
        pass

