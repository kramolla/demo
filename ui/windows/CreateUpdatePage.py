from PySide6.QtWidgets import QWidget
from db.connection import session
from db.models import *

from ui.widgets.edit_partner_dialog import Ui_EditPartnerDialog

class CreateUpdatePage(QWidget, Ui_EditPartnerDialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)