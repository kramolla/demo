from PySide6.QtWidgets import QWidget

from database.models import PartnerModel
from ui.widgets.partner_card import Ui_PartnerCard

class PartnerCard(QWidget, Ui_PartnerCard):
    def __init__(self, partner: PartnerModel, orders, discount, go_to_orders_page, go_to_create_update_page):
        super().__init__()

        self.setupUi(self)

        self.PartnerTypeAndName.setText(partner.type + " | " + partner.name)
        self.BossName.setText(partner.boss_name)
        self.PhoneNumber.setText(partner.phone_number)
        self.Rank.setText(str(partner.rate))
        self.DiscountPercentage.setText(str(discount) + "%")

        # Подключаем сигналы для кнопок.
        self.GetOrdersListButton.clicked.connect(lambda: go_to_orders_page(orders))
        self.PartnerTypeAndName.clicked.connect(lambda: go_to_create_update_page(partner))
        self.BossName.clicked.connect(lambda: go_to_create_update_page(partner))
        self.PhoneNumber.clicked.connect(lambda: go_to_create_update_page(partner))
        self.Rank.clicked.connect(lambda: go_to_create_update_page(partner))
        self.DiscountPercentage.clicked.connect(lambda: go_to_create_update_page(partner))