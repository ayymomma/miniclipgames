import sys
import json

from PyQt5 import Qt, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox

from customWidgets.buttons.bottomButtons import BottomButtons
from customWidgets.buttons.exitButton import ExitButton
from customWidgets.buttons.settingsButton import SettingsButton
from customWidgets.frames.gamesFrame import GamesFrame

style = """
QMainWindow {{
    background-color: {primary_color};
}}
"""


class MainWindow(QMainWindow):
    exit_click = pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.centralWidget = QtWidgets.QWidget(self)
        self.theme = self.readTheme()
        self.gamesFrame = GamesFrame(self.centralWidget, self.theme)
        self.bottomButtons = BottomButtons(self.centralWidget, self.theme)
        self.logoLabel = QLabel(self.centralWidget)
        self.setCentralWidget(self.centralWidget)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Miniclip Games")
        self.setStyleSheet(style.format(primary_color=self.theme['primary']))

        self.bottomButtons.exit_click_signal.connect(lambda: self.onExitClick())

        font = QFont("Helvetica")
        font.setWeight(30)
        font.setPixelSize(80)
        font.setBold(True)
        self.logoLabel.setFont(font)
        self.logoLabel.setText("MINICLIP")
        self.logoLabel.setGeometry(40, 70, 400, 70)
        self.logoLabel.setStyleSheet("color: {0}".format(self.theme['on-primary']))
        self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_Escape:
            sys.exit(0)

    def readTheme(self):
        with open('customWidgets/themes/theme.json', 'r') as f:
            json_theme = json.load(f)
        return json_theme

    @QtCore.pyqtSlot()
    def onExitClick(self):
        quit_message = "Are you sure you want to exit the program?"
        if QMessageBox.question(self, 'Exit',
                                quit_message, QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
            sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mini = MainWindow()
    mini.show()
    sys.exit(app.exec())
