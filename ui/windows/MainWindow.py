from PySide6.QtWidgets import QMainWindow, QStackedWidget

from ui.windows.CreateUpdatePage import CreateUpdatePage
from ui.windows.OrdersPage import OrdersPage
from ui.windows.PartnersPage import PartnersPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 250, 1000, 600)
        self.setWindowTitle("Список партнёров")

        # Создаем QStackedWidget
        self.stacked_widget = QStackedWidget()

        # Создаем несколько виджетов для отображения
        self.page2 = OrdersPage(self.go_to_partners_page)
        self.page3 = CreateUpdatePage(self.go_to_partners_page)
        self.page1 = PartnersPage(self.go_to_orders_page, self.go_to_create_update_page)

        # Добавляем виджеты в QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        # Устанавливаем QStackedWidget как центральный виджет
        self.setCentralWidget(self.stacked_widget)

        # Подключаем сигнал currentChanged к методу изменения заголовка
        self.stacked_widget.currentChanged.connect(self.update_window_title)

    def go_to_partners_page(self):
        self.page1.fill_list()
        self.stacked_widget.setCurrentIndex(0)

    def go_to_orders_page(self, orders):
        self.page2.fill_list(orders)
        self.stacked_widget.setCurrentIndex(1)

    def go_to_create_update_page(self, partner):
        self.page3.fill_form(partner)
        self.stacked_widget.setCurrentIndex(2)

    def update_window_title(self, index):
        """Метод для обновления заголовка окна в зависимости от текущей страницы."""
        if index == 0:
            self.setWindowTitle("Список партнёров")
        elif index == 1:
            self.setWindowTitle("Список заказов партнёра")
        elif index == 2:
            self.setWindowTitle("Создание/изменение партнёра")