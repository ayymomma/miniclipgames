import os
import sys
import json
import threading
import time
import psutil as psutil

from PyQt5 import Qt, QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox

from Audio.audioManager import AudioManager
from Audio.voiceManager import VoiceManager
from Video.videoManager import VideoManager
from customWidgets.buttons.bottomButtons import BottomButtons
from customWidgets.buttons.videoButton import VideoButton
from customWidgets.buttons.voiceButton import VoiceButton
from customWidgets.frames.gamesFrame import GamesFrame

style = """
QMainWindow {{
    background-color: {primary_color};
}}
QMessageBox {{
    background-color: {primary_color};
}}

QMessageBox QLabel {{
    color: {on_primary};
}}

QMessageBox QPushButton {{
    background-color: {secondary_color};
    color: {on_secondary};
    font-size: 18px;
    border-radius: 15px;
    min-height: 30px;
    min-width: 60px;
    margin-left: 10px;
    margin-right: 10px;
}}
QPushButton:hover {{
    background-color: {secondary_variant_color};
}}
QPushButton:pressed {{
    background-color: {secondary_color};
}}
"""


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.centralWidget = QtWidgets.QWidget(self)
        self.theme = None
        self.readTheme()
        self.gamesFrame = GamesFrame(self.centralWidget, self.theme)
        self.bottomButtons = BottomButtons(self.centralWidget, self.theme)
        self.voiceButton = VoiceButton(self.centralWidget)
        self.videoButton = VideoButton(self.centralWidget)
        self.logoLabel = QLabel(self.centralWidget)
        self.audioManager = AudioManager()
        self.voiceManager = VoiceManager()
        self.videoManager = VideoManager()
        self.voiceThread = threading.Thread(target=self.voiceManager.start)
        self.voiceThread.start()
        # self.videoThread = threading.Thread(target=self.videoManager.startStream)
        # self.videoThread.start()
        self.videoThread = None
        self.videoOn = False
        self.setCentralWidget(self.centralWidget)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Miniclip Games")
        self.setStyleSheet(style.format(primary_color=self.theme['primary'],
                                        secondary_color=self.theme['secondary'],
                                        secondary_variant_color=self.theme['secondary-variant'],
                                        on_secondary=self.theme['on-secondary'],
                                        on_primary=self.theme['on-primary']))
        self.voiceButton.setButtonStyle(self.theme['secondary'], self.theme['on-secondary'], self.theme['border-color'])
        self.videoButton.setButtonStyle(self.theme['secondary'], self.theme['on-secondary'], self.theme['border-color'])
        self.bottomButtons.exit_click_signal.connect(lambda: self.onExitClick())
        self.bottomButtons.settings_click_signal.connect(lambda: self.onSettingsClick())
        self.gamesFrame.onGameClick_signal.connect(lambda: self.onGameClick())

        font = QFont("Helvetica")
        font.setWeight(30)
        font.setPixelSize(80)
        font.setBold(True)
        self.logoLabel.setFont(font)
        self.logoLabel.setText("MINICLIP")
        self.logoLabel.setGeometry(60, 70, 400, 70)
        self.logoLabel.setStyleSheet("color: {0}".format(self.theme['on-primary']))
        self.showFullScreen()

        self.voiceButton.setGeometry(70, 850, 150, 50)
        self.videoButton.setGeometry(300, 850, 150, 50)
        self.videoButton.click_signal.connect(lambda: self.onVideoClick())

    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_Escape:
            self.onExitClick()

    def readTheme(self):
        with open('customWidgets/themes/theme.json', 'r') as f:
            self.theme = json.load(f)

    @QtCore.pyqtSlot()
    def onExitClick(self):
        self.audioManager.playSoundButtonClick()
        quit_message = "Are you sure you want to exit?"
        if QMessageBox.question(self, ' ',
                                quit_message, QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
            self.audioManager.playSoundButtonClick()
            self.voiceManager.quitFlag = False
            self.videoManager.runFlag = False
            print(self.voiceManager.quitFlag)
            time.sleep(0.2)
            sys.exit(0)
        else:
            self.audioManager.playSoundButtonClick()

    @QtCore.pyqtSlot()
    def onSettingsClick(self):
        self.audioManager.playSoundButtonClick()

    @QtCore.pyqtSlot()
    def onGameClick(self):
        self.audioManager.playSoundButtonClick()

    @QtCore.pyqtSlot()
    def onVideoClick(self):
        if self.videoOn:
            print("Video off")
            self.videoManager.runFlag = False
            self.videoOn = False
        else:
            print("Video on")
            self.videoManager.runFlag = True
            self.videoThread = threading.Thread(target=self.videoManager.startStream)
            self.videoThread.start()
            self.videoOn = True


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mini = MainWindow()
    mini.show()
    returnValue = app.exec()
    if returnValue is not None:
        kill_proc_tree(os.getpid())
        sys.exit(returnValue)
