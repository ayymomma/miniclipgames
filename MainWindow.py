import sys
import json

from PyQt5 import Qt, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from customWidgets.frames.gamesFrame import GamesFrame

style = """
QMainWindow {{
    background-color: {primary_color};
}}
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.centralWidget = QtWidgets.QWidget(self)
        self.theme = self.readTheme()
        self.gamesFrame = GamesFrame(self.centralWidget, self.theme)

        self.setCentralWidget(self.centralWidget)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Miniclip Games")
        self.setStyleSheet(style.format(primary_color=self.theme['primary']))
        self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_Escape:
            sys.exit(0)

    def readTheme(self):
        with open('customWidgets/themes/theme.json', 'r') as f:
            json_theme = json.load(f)
        return json_theme


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mini = MainWindow()
    mini.show()
    sys.exit(app.exec())
