from PySide6.QtWidgets import QWidget
from database.connection import session
from database.models import *

from ui.widgets.orders_page import Ui_OrdersPage

class OrdersList(QWidget, Ui_OrdersPage):
    def __init__(self):
        super().__init__()

        self.setupUi(self)