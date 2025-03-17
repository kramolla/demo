from PySide6.QtWidgets import QWidget
from db.connection import session
from db.models import *

from ui.widgets.order_card import Ui_OrderCard

class OrderCard(QWidget, Ui_OrderCard):
    def __init__(self):
        super().__init__()

        self.setupUi(self)