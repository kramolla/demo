from PySide6.QtWidgets import QWidget
from db.connection import session
from db.models import *

from ui.widgets.orders_page import Ui_OrdersPage

class OrdersList(QWidget, Ui_OrdersPage):
    def __init__(self):
        super().__init__()

        self.setupUi(self)