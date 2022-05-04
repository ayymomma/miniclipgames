from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton

style = """
QPushButton {{
    background-color: {secondary_color};
    color: {on_secondary};
    font-size: 18px;
    border-radius: 25px;
    border: 2px solid;
    border-color: {border_color};
}}
QPushButton:pressed {{
    background-color: {secondary_color};
}}
"""


class VoiceButton(QPushButton):
    click_signal = pyqtSignal()

    def __init__(self, parent):
        super(VoiceButton, self).__init__(parent)
        self.clicked.connect(self.onClick)
        self.setupUi()

    def setupUi(self):
        font = QFont("Helvetica")
        font.setWeight(30)
        font.setPixelSize(80)
        font.setBold(True)
        self.setFont(font)
        self.setText("Voice Off")
        self.setMinimumSize(150, 50)
        self.setMaximumSize(150, 50)

    def setButtonStyle(self, background_color, on_secondary, border_color):
        self.setStyleSheet(style.format(secondary_color=background_color,
                                        on_secondary=on_secondary,
                                        border_color=border_color))

    def enterEvent(self, event: QtCore.QEvent):
        super(VoiceButton, self).enterEvent(event)
        self.setMinimumSize(170, 50)
        self.setMaximumSize(170, 50)
        self.setGeometry(self.pos().x() - 10, self.pos().y(), self.width() + 10, self.height())

    def leaveEvent(self, event: QtCore.QEvent):
        super(VoiceButton, self).leaveEvent(event)
        self.setMinimumSize(150, 50)
        self.setMaximumSize(150, 50)
        self.setGeometry(self.pos().x() + 10, self.pos().y(), self.width() - 10, self.height())

    def onClick(self):
        self.click_signal.emit()
        self.setText("Voice On") if self.text() == "Voice Off" else self.setText("Voice Off")
