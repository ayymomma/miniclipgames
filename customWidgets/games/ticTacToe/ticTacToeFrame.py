from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSignal, Qt, QRect
from PyQt5.QtGui import QFont, QPixmap, QColor, QImage, QBrush, QPainter, QWindow
from PyQt5.QtWidgets import QFrame, QLabel, QSizePolicy

style = """
QFrame {
    max-width: 280px;
    max-height: 280px;
    min-width: 280px;
    min-height: 280px;
}
"""
style_hover = """
QFrame {
    max-width: 300px;
    max-height: 300px;
    min-width: 300px;
    min-height: 300px;
}
"""


class TicTacToeFrame(QFrame):
    click_signal = pyqtSignal()

    def __init__(self, parent, theme):
        super(TicTacToeFrame, self).__init__(parent)
        # self.textLabel = QLabel(self)
        self.image = QLabel(self)
        self.setupUi(theme)

    def setupUi(self, theme):
        self.setStyleSheet(style)
        pixmap = QPixmap("resources\\images\\ticTacToe2.png")
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def enterEvent(self, event: QtCore.QEvent):
        super(TicTacToeFrame, self).enterEvent(event)
        self.setStyleSheet(style_hover)

    def leaveEvent(self, event: QtCore.QEvent):
        super(TicTacToeFrame, self).leaveEvent(event)
        self.setStyleSheet(style)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        self.click_signal.emit()

    # function to alter image
