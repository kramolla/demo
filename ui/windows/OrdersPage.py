from PySide6.QtWidgets import QWidget
from database.connection import session
from database.models import *

from ui.widgets.orders_page import Ui_OrdersPage
from ui.windows.OrderCard import OrderCard


class OrdersPage(QWidget, Ui_OrdersPage):
    def __init__(self, go_to_partners_page):
        super().__init__()

        self.setupUi(self)

        self.BackButton.clicked.connect(go_to_partners_page)

    def fill_list(self, orders):
        """Обновляет список заказов."""
        while self.list.count() > 0:
            item = self.list.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        for order in orders:
            product = session.query(ProductModel).filter_by(id=order.product).scalar()
            card = OrderCard(product.name, order)
            self.list.addWidget(card)