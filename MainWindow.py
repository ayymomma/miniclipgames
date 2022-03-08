import sys

from PyQt5 import Qt, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

from customWidgets.frames.gamesFrame import GamesFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.centralWidget = QtWidgets.QWidget(self)
        self.gamesFrame = GamesFrame(self.centralWidget)

        self.setCentralWidget(self.centralWidget)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Miniclip Games")
        self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_Escape:
            sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mini = MainWindow()
    mini.show()
    sys.exit(app.exec())
