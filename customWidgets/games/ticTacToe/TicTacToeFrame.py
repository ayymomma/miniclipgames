from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

style = """
QFrame {{
   background-color: {primary_color};
   border-radius: 10px;
   border-style: None;
   max-width: 300px;
}}
"""


class TicTacToeFrame(QFrame):
    def __init__(self, parent, theme):
        super(TicTacToeFrame, self).__init__(parent)
        self.textLabel = QLabel(self)
        self.setupUi(theme)

    def setupUi(self, theme):
        self.setStyleSheet(style.format(primary_color=theme['primary'],
                                        primary_variant_color=theme['primary-variant']))
        font = QFont("Helvetica")
        font.setWeight(30)
        font.setPixelSize(30)
        font.setBold(True)
        self.textLabel.setFont(font)
        self.textLabel.setText("TIC TAC TOE")
        self.textLabel.setGeometry(55, 120, 200, 50)
        self.textLabel.setStyleSheet("color: {0}".format(theme['on-primary']))
