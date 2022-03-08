from PyQt5.QtWidgets import QFrame

style = """
QFrame {
   background-color: #30363F;
   border-style: solid;
   border-width: 2px;
   border-radius: 10px;
   border-color: #606368;
}
"""


class NormalGames(QFrame):
    def __init__(self, parent):
        super(NormalGames, self).__init__(parent)
        self.setStyleSheet(style)

        self.setupUi()

    def setupUi(self):
        pass
