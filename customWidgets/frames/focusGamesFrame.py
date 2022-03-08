from PyQt5.QtWidgets import QFrame


class FocusGames(QFrame):
    def __init__(self, parent):
        super(FocusGames, self).__init__(parent)
        self.setStyleSheet("background-color: #30000F")

        self.setupUi()

    def setupUi(self):
        pass
