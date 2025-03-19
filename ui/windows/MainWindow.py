from PySide6.QtWidgets import QMainWindow, QStackedWidget

from ui.windows.PartnersList import PartnersPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Смена контента в окне")

        # Создаем QStackedWidget
        self.stacked_widget = QStackedWidget()

        # Создаем несколько виджетов для отображения
        self.page1 = PartnersPage()
        # self.page2 = QWidget()

        # Добавляем виджеты в QStackedWidget
        self.stacked_widget.addWidget(self.page1)
        #self.stacked_widget.addWidget(self.page2)

        # Устанавливаем QStackedWidget как центральный виджет
        self.setCentralWidget(self.stacked_widget)

    def go_to_page1(self):
        self.stacked_widget.setCurrentIndex(0)

    def go_to_page2(self):
        self.stacked_widget.setCurrentIndex(1)