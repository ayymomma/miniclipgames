from PyQt5.QtWidgets import QPushButton


class TicTacToeCell(QPushButton):

    def __init__(self, parent):
        super(TicTacToeCell, self).__init__(parent)
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

    def __repr__(self):
        return f'[{self.text}]'
