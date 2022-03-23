from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel

style = """
QFrame {{
   background-color: {primary_color};
   border-radius: 10px;
   border-style: None;
   max-width: 280px;
}}
QFrame:hover {{
    background-color: {primary_second_variant};
}}
QLabel {{
    background-color: None;
}}
"""


class TicTacToeFrame(QFrame):
    click_signal = pyqtSignal()

    def __init__(self, parent, theme):
        super(TicTacToeFrame, self).__init__(parent)
        self.textLabel = QLabel(self)
        self.setupUi(theme)

    def setupUi(self, theme):
        self.setStyleSheet(style.format(primary_color=theme['primary'],
                                        primary_variant_color=theme['primary-variant'],
                                        primary_second_variant=theme['primary-second-variant']))
        font = QFont("Helvetica")
        font.setWeight(30)
        font.setPixelSize(30)
        font.setBold(True)
        self.textLabel.setFont(font)
        self.textLabel.setText("TIC TAC TOE")
        self.textLabel.setGeometry(45, 120, 190, 50)
        self.textLabel.setStyleSheet("color: {0}".format(theme['on-primary']))

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        self.click_signal.emit()
