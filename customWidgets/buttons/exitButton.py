from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton

style = """
QPushButton {{
    background-color: {secondary_color};
    color: {on_secondary};
    font-size: 18px;
    border-radius: 5px;
    min-height: 50px;
    min-width: 110px;
}}
QPushButton:hover {{
    background-color: {secondary_variant_color};
}}
QPushButton:pressed {{
    background-color: {secondary_color};
}}
"""


class ExitButton(QPushButton):
    click_signal = pyqtSignal()

    def __init__(self, parent):
        super(ExitButton, self).__init__(parent)
        self.clicked.connect(self.onClick)
        self.setupUi()

    def setupUi(self):
        self.setText("QUIT")

    def setButtonStyle(self, background_color, on_secondary, hover_color):
        self.setStyleSheet(style.format(secondary_color=background_color,
                                        on_secondary=on_secondary,
                                        secondary_variant_color=hover_color))

    def onClick(self):
        self.click_signal.emit()
