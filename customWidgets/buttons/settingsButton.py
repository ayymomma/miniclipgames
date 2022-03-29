from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton

style = """
QPushButton {{
    background-color: {secondary_color};
    color: {on_secondary};
    font-size: 18px;
    border-radius: 25px;
}}
QPushButton:pressed {{
    background-color: {secondary_color};
}}
"""


class SettingsButton(QPushButton):
    click_signal = pyqtSignal()

    def __init__(self, parent):
        super(SettingsButton, self).__init__(parent)
        self.clicked.connect(self.onClick)
        self.setupUi()

    def setupUi(self):
        self.setText("SETTINGS")
        self.setMinimumSize(150, 50)
        self.setMaximumSize(150, 50)

    def setButtonStyle(self, background_color, on_secondary, hover_color):
        self.setStyleSheet(style.format(secondary_color=background_color,
                                        on_secondary=on_secondary))

    def enterEvent(self, event: QtCore.QEvent):
        super(SettingsButton, self).enterEvent(event)
        self.setMinimumSize(170, 50)
        self.setMaximumSize(170, 50)
        self.setGeometry(self.pos().x() - 10, self.pos().y(), self.width() + 10, self.height())

    def leaveEvent(self, event: QtCore.QEvent):
        super(SettingsButton, self).leaveEvent(event)
        self.setMinimumSize(150, 50)
        self.setMaximumSize(150, 50)
        self.setGeometry(self.pos().x() + 10, self.pos().y(), self.width() - 10, self.height())


    def onClick(self):
        self.click_signal.emit()
