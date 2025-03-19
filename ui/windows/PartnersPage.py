from PySide6.QtCore import QSize
from PySide6.QtWidgets import QWidget, QListWidgetItem
from sqlalchemy import func

from database.connection import session
from database.models import *

from ui.windows.PartnerCard import PartnerCard

from ui.widgets.partners_page import Ui_PartnersPage

class PartnersPage(QWidget, Ui_PartnersPage):
    def __init__(self, go_to_orders_page, go_to_create_update_page):
        super().__init__()

        self.setupUi(self)

        self.addPartnerButton.clicked.connect(lambda: go_to_create_update_page(None))

        self.go_to_orders_page = go_to_orders_page
        self.go_to_create_update_page = go_to_create_update_page

        self.fill_list()

    def fill_list(self):
        """Обновление списка партнёров."""
        # while self.list.count() > 0:
        #     item = self.list.takeAt(0)
        #     widget = item.widget()
        #     if widget is not None:
        #         widget.deleteLater()

        self.listWidget.clear()

        # Загружаем данные из базы.
        partners = session.query(PartnerModel).order_by(PartnerModel.id).all()

        # Создаём карточки.
        for partner in partners:
            discount = calculate_discount(partner.id)  # Рассчитываем скидку для партнёра.
            orders = session.query(OrderModel).filter_by(partner=partner.id).all()

            card = PartnerCard(partner, orders, discount, self.go_to_orders_page, self.go_to_create_update_page)

            # list.addWidget(card)

            item = QListWidgetItem()
            item.setSizeHint(QSize(900, 200))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, card)

# Функция для расчёта скидки на основе общего количества заказов партнёра.
def calculate_discount(partner_id):
    # Получаем общее количество заказанных единиц продукции для данного партнёра.
    total_quantity = session.query(func.sum(OrderModel.count)).filter(OrderModel.partner == partner_id).scalar() or 0
    # Логика определения скидки в зависимости от объёма.
    if total_quantity > 300000:
        return 15
    elif total_quantity > 50000:
        return 10
    elif total_quantity > 10000:
        return 5
    else:
        return 0