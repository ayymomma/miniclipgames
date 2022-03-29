
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QFrame, QLabel, QSizePolicy

style = """
QFrame {{
    background-color: {secondary_color};
    border-radius: 25px;
    border: 2px solid;
    border-color: {border_color};
}}
QLabel {{
    border: None;
    background-color: None;
    color: {text_color};
    font-size: {font_size};
    font-weight: {font_wight};
}}
#name {{
    border: None;
    background-color: None;
    color: {on_secondary};
    font-size: 20px;
    font-weight: 20px;
}}
"""


class PlayerInfo(QFrame):
    def __init__(self, parent, image, sign, name, theme):
        super(PlayerInfo, self).__init__(parent)
        self.avatarIcon = QLabel(self)
        self.signIcon = QLabel(self)
        self.name = QLabel(self)
        self.setupUi(image, sign, name, theme)

    def setupUi(self, image, sign, name, theme):
        self.setMinimumSize(130, 180)
        self.setMaximumSize(50, 100)
        if sign == "X":
            self.setStyleSheet(style.format(secondary_color=theme["primary-second-variant"],
                                            border_color=theme["border-color"],
                                            text_color=theme["x-color"],
                                            on_secondary=theme["on-secondary"],
                                            font_size="30px",
                                            font_wight="70px"))
        else:
            self.setStyleSheet(style.format(secondary_color=theme["primary-second-variant"],
                                            border_color=theme["border-color"],
                                            text_color=theme["o-color"],
                                            on_secondary=theme["on-secondary"],
                                            font_size="30px",
                                            font_wight="70px"))
        self.signIcon.setGeometry(QRect(int(self.width()/2)-10, 130, 40, 40))
        font = QFont("Helvetica")
        font.setBold(True)
        self.setFont(font)
        self.signIcon.setText(sign)

        self.name.setObjectName("name")
        self.name.setAlignment(Qt.AlignCenter)
        self.name.setGeometry(QRect(int(self.width()/2)-35, 90, 70, 30))
        self.name.setText(name)


        pixmap = QPixmap("resources\\images\\" + image)
        self.avatarIcon.setPixmap(pixmap)
        self.avatarIcon.setGeometry(QRect(int(self.width()/2)-25, 30, 50, 50))
        self.avatarIcon.setScaledContents(True)
        self.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)