import threading

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QRect, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QPushButton

from Audio.voiceManager import VoiceManager
from customWidgets.buttons.resetButton import ResetButton
from customWidgets.games.ticTacToe.playerInfo import PlayerInfo
from customWidgets.games.ticTacToe.ticTacToeBoard import TicTacToeBoard

style = """
QDialog {{
    background-color: {primary_color};
}}
QLabel {{
    background-color: None;
    color: {on_primary};
    font-size: 20px;
    font-weight: 20px;
}}
"""


class TicTacToe(QDialog):

    def __init__(self, parent, theme):
        super(TicTacToe, self).__init__(parent)
        self.board = TicTacToeBoard(self, theme)
        self.resetButton = ResetButton(self)
        self.playerInfo = PlayerInfo(self, "P.png", "X", "Player", theme)
        self.botInfo = PlayerInfo(self, "B.png", "O", "Bot", theme)
        self.playerState = QLabel(self)
        self.botState = QLabel(self)
        self.voiceManager = VoiceManager()
        self.setupUi(theme)

    def setupUi(self, theme):
        self.setWindowTitle("Tic Tac Toe")
        self.setMaximumSize(600, 900)
        self.setMinimumSize(600, 900)
        self.setStyleSheet(style.format(primary_color=theme['primary'], on_primary=theme["on-primary"]))

        self.board.win_signal.connect(lambda value: self.setWinner(value))
        self.board.reset_signal.connect(lambda: self.resetWinner())

        self.resetButton.setButtonStyle(theme['secondary'], theme['on-secondary'], theme['border-color'])
        self.resetButton.clicked.connect(lambda: self.board.reset())
        self.resetButton.setGeometry(QRect(225, 825, 150, 50))

        self.playerInfo.setGeometry(130, 20, 0, 0)
        self.botInfo.setGeometry(340, 20, 0, 0)

        self.playerState.setGeometry(QRect(150, 210, 92, 20))
        self.playerState.setAlignment(Qt.AlignCenter)
        self.botState.setGeometry(QRect(360, 210, 92, 20))
        self.botState.setAlignment(Qt.AlignCenter)
        self.show()

    def setWinner(self, value):
        if value == "Player win":
            self.playerState.setText("Winner")
            threading.Thread(target=self.voiceManager.textToSpeech, args=("Player win", )).start()
            self.botState.setText("Loser")
            return
        if value == "Computer win":
            self.playerState.setText("Loser")
            self.botState.setText("Winner")
            threading.Thread(target=self.voiceManager.textToSpeech, args=("Computer win", )).start()
            return
        self.playerState.setText("Tie")
        self.botState.setText("Tie")

    def resetWinner(self):
        self.playerState.setText("")
        self.botState.setText("")

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.board.close()
        super().closeEvent(a0)
