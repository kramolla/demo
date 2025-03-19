from PySide6.QtWidgets import QWidget
from database.models import *

from ui.widgets.order_card import Ui_OrderCard

class OrderCard(QWidget, Ui_OrderCard):
    def __init__(self, product_name, order: OrderModel):
        super().__init__()

        self.setupUi(self)

        self.product_name.setText(product_name)
        self.quantity_of_products.setText(str(order.count))
        self.date_of_create.setText(str(order.date))