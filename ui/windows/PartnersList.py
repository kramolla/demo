from PySide6.QtWidgets import QWidget

from db.connection import session
from db.models import *

from ui.windows.OrdersList import OrdersList
from ui.windows.CreateUpdatePage import CreateUpdatePage
from ui.windows.PartnerCard import PartnerCard

from ui.widgets.partner_list import Ui_PartnerList

class PartnersPage(QWidget, Ui_PartnerList):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def show_history(self, partner_id):
        """Открытие окна истории продаж для конкретного партнёра."""
        history_window = PartnerHistory(partner_id)
        self.history_windows.append(history_window)  # Сохраняем ссылку на окно.
        history_window.show()
        history_window.destroyed.connect(lambda: self.cleanup_history_windows(history_window))

    def add_partner(self):
        """Открытие окна для добавления нового партнёра."""
        dialog = EditPartnerDialog()
        if dialog.exec():
            self.refresh_list()  # Обновляем список после добавления.

    def edit_partner(self, partner):
        """Открытие окна для редактирования информации о партнёре."""
        dialog = EditPartnerDialog(partner)
        if dialog.exec():
            self.refresh_list()  # Обновляем список после изменения.

    def refresh_list(self):
        """Обновление списка партнёров."""
        # Удаляем старые виджеты из лейаута.
        while self.content_layout.count() > 0:
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        # Перезагружаем данные из базы.
        self.partners = session.query(PartnerModel).order_by(PartnerModel.id).all()

        # Создаём карточки заново.
        for partner in self.partners:
            discount = calculate_discount(partner.id)  # Рассчитываем скидку для партнёра.
            card = PartnerCard(partner=partner, discount=discount)
            self.content_layout.addWidget(card)

            # Подключаем сигналы для кнопок.
            card.show_history_button.clicked.connect(lambda _, p=partner: self.show_history(p.id))
            card.edit_partner_button.clicked.connect(lambda _, p=partner: self.edit_partner(p))