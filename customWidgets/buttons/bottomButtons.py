from PyQt5 import QtCore
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtWidgets import QFrame, QHBoxLayout

from customWidgets.buttons.exitButton import ExitButton
from customWidgets.buttons.settingsButton import SettingsButton


class BottomButtons(QFrame):
    exit_click_signal = pyqtSignal()
    settings_click_signal = pyqtSignal()

    def __init__(self, parent, theme):
        super(BottomButtons, self).__init__(parent)

        self.exitButton = ExitButton(parent)
        self.settingsButton = SettingsButton(parent)
        self.buttonsLayout = QHBoxLayout()
        self.setupUi(theme)

    def setupUi(self, theme):
        self.setGeometry(QRect(80, 970, 300, 70))
        self.buttonsLayout.setSpacing(70)

        self.exitButton.setButtonStyle(theme['secondary'], theme['on-secondary'], theme['secondary-variant'])
        self.exitButton.click_signal.connect(lambda: self.onExitClick())
        self.settingsButton.setButtonStyle(theme['secondary'], theme['on-secondary'], theme['secondary-variant'])
        self.settingsButton.click_signal.connect(lambda: self.onSettingsClick())

        self.buttonsLayout.addWidget(self.exitButton)
        self.buttonsLayout.addWidget(self.settingsButton)
        self.setLayout(self.buttonsLayout)

    @QtCore.pyqtSlot()
    def onExitClick(self):
        self.exit_click_signal.emit()

    @QtCore.pyqtSlot()
    def onSettingsClick(self):
        self.settings_click_signal.emit()

