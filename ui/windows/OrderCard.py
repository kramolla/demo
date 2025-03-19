from PySide6.QtWidgets import QWidget
from database.connection import session
from database.models import *

from ui.widgets.order_card import Ui_OrderCard

class OrderCard(QWidget, Ui_OrderCard):
    def __init__(self):
        super().__init__()

        self.setupUi(self)