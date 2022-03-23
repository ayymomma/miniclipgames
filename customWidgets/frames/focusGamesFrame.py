from PyQt5.QtWidgets import QFrame, QGraphicsBlurEffect

style = """
QFrame {{
   background-color: {primary_variant_color};
   border-radius: 10px;
   border-color: {secondary_color};
}}
"""


class FocusGames(QFrame):
    def __init__(self, parent, theme):
        super(FocusGames, self).__init__(parent)
        self.setStyleSheet(style)
        self.blur_effect = QGraphicsBlurEffect()

        self.setupUi(theme)

    def setupUi(self, theme):
        self.setStyleSheet(
            style.format(primary_variant_color=theme['primary-variant'],
                         secondary_color=theme['secondary']))
        self.blur_effect.setBlurRadius(1.4)
        self.setGraphicsEffect(self.blur_effect)
