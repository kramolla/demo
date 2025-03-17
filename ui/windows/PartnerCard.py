from PySide6.QtWidgets import QWidget

from ui.widgets.partner_card import Ui_PartnerCard

class PartnerCard(QWidget, Ui_PartnerCard):
    def __init__(self):
        super().__init__()

        self.setupUi(self)