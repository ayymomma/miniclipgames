from PyQt5 import QtCore
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtWidgets import QFrame, QGraphicsBlurEffect, QHBoxLayout

from customWidgets.games.ticTacToe.TicTacToeFrame import TicTacToeFrame
from customWidgets.games.ticTacToe.ticTacToe import TicTacToe

style = """
QFrame {{
   background-color: {primary_variant_color};
   border-radius: 10px;
   border-color: {secondary_color};
}}
"""


class FocusGames(QFrame):
    onTicTacToeClick_signal = pyqtSignal()

    def __init__(self, parent, theme):
        super(FocusGames, self).__init__(parent)
        self.setStyleSheet(style)

        self.gamesLayout = QHBoxLayout()
        self.ticTacToeFrame = TicTacToeFrame(self, theme)
        self.ticTacToeFrame1 = TicTacToeFrame(self, theme)
        self.ticTacToeFrame2 = TicTacToeFrame(self, theme)
        self.ticTacToeFrame3 = TicTacToeFrame(self, theme)

        self.ticTacToe = None

        self.setupUi(theme, parent)

    def setupUi(self, theme, parent):
        self.setStyleSheet(
            style.format(primary_variant_color=theme['primary-variant'],
                         secondary_color=theme['secondary']))

        self.gamesLayout.setGeometry(QRect(0, 0, self.width(), self.height()))
        self.gamesLayout.addWidget(self.ticTacToeFrame)
        self.gamesLayout.addWidget(self.ticTacToeFrame1)
        self.gamesLayout.addWidget(self.ticTacToeFrame2)
        self.gamesLayout.addWidget(self.ticTacToeFrame3)
        self.setLayout(self.gamesLayout)

        self.ticTacToeFrame.click_signal.connect(lambda: self.onTicTacToeClick(parent, theme))
        self.ticTacToeFrame1.click_signal.connect(lambda: self.onTicTacToeClick(parent, theme))
        self.ticTacToeFrame2.click_signal.connect(lambda: self.onTicTacToeClick(parent, theme))
        self.ticTacToeFrame3.click_signal.connect(lambda: self.onTicTacToeClick(parent, theme))

    @QtCore.pyqtSlot()
    def onTicTacToeClick(self, parent, theme):
        self.ticTacToe = TicTacToe(parent, theme)
        self.onTicTacToeClick_signal.emit()
