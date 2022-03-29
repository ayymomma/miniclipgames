from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton


class TicTacToeCell(QPushButton):
    click_signal = pyqtSignal(int)
    index = None

    def __init__(self, parent, index):
        super(TicTacToeCell, self).__init__(parent)
        self.index = index
        self.text = ''

    def captured(self):
        return self.text

    def capture(self, symbol):
        self.text = symbol
        self.setText(symbol)
        self.setEnabled(False)

    def reset(self):
        self.text = ''
        self.setText(self.text)
        self.setEnabled(True)

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        super(TicTacToeCell, self).mouseReleaseEvent(e)
        if self.isEnabled():
            self.click_signal.emit(self.index)


    def __repr__(self):
        return f'[{self.text}]'
