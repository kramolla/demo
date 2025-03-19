from PySide6.QtWidgets import QWidget, QMessageBox
from database.connection import session
from database.models import *

from ui.widgets.create_update_page import Ui_CreateUpdatePage

class CreateUpdatePage(QWidget, Ui_CreateUpdatePage):
    def __init__(self, go_to_partners_page):
        super().__init__()

        self.setupUi(self)

        self.partner: PartnerModel = PartnerModel()

        self.SaveButton.clicked.connect(self.save_partner)
        self.CancelButton.clicked.connect(go_to_partners_page)

        self.go_to_partners_page = go_to_partners_page

    def fill_form(self, partner):
        """Устанавливает partner и обновляет список заказов."""
        self.partner = partner

        if partner is not None:
            self.TypeInput.setCurrentText(partner.type)
            self.NameInput.setText(partner.name)
            self.BossNameInput.setText(partner.boss_name)
            self.EmailInput.setText(partner.email)
            self.PhoneNumberInput.setText(partner.phone_number)
            self.AddressInput.setText(partner.address)
            self.InnInput.setText(partner.inn)
            self.RateInput.setText(str(partner.rate))
        else:
            self.TypeInput.setCurrentText("ООО")
            self.NameInput.setText("")
            self.BossNameInput.setText("")
            self.EmailInput.setText("")
            self.PhoneNumberInput.setText("")
            self.AddressInput.setText("")
            self.InnInput.setText("")
            self.RateInput.setText("")

    def save_partner(self):
        """Сохранение данных о партнёре в базу данных."""
        try:
            # Проверяем, что обязательные поля заполнены.
            if not self.NameInput.text().strip():
                raise ValueError("Поле 'Имя партнёра' не может быть пустым.")

            if not self.BossNameInput.text().strip():
                raise ValueError("Поле 'Имя директора' не может быть пустым.")

            if not self.EmailInput.text().strip():
                raise ValueError("Поле 'Электронная почта' не может быть пустым.")

            phone_number = self.PhoneNumberInput.text()
            phone_number = phone_number.replace(" ", "").replace("_", "")

            if len(phone_number) != 10:
                raise ValueError("Поле 'Номер телефона' должно содержать 10 чисел.")

            if not self.AddressInput.text().strip():
                raise ValueError("Поле 'Адрес' не может быть пустым.")

            inn = self.InnInput.text()
            inn = inn.replace(" ", "").replace("_", "")

            if len(inn) != 10:
                raise ValueError("Поле 'ИНН' должно содержать 10 чисел.")

            if not self.RateInput.text().isdigit():
                raise ValueError("Рейтинг должен быть числом.")

            if self.partner:
                # Обновление существующего партнёра.
                self.partner.type = self.TypeInput.currentText()
                self.partner.name = self.NameInput.text()
                self.partner.address = self.AddressInput.text()
                self.partner.inn = self.InnInput.text()
                self.partner.boss_name = self.BossNameInput.text()
                self.partner.phone_number = self.PhoneNumberInput.text()
                self.partner.email = self.EmailInput.text()
                self.partner.rate = int(self.RateInput.text())
            else:
                # Добавление нового партнёра.
                new_partner = PartnerModel(
                    type=self.TypeInput.currentText(),
                    name=self.NameInput.text(),
                    address=self.AddressInput.text(),
                    inn=self.InnInput.text(),
                    boss_name=self.BossNameInput.text(),
                    phone_number=self.PhoneNumberInput.text(),
                    email=self.EmailInput.text(),
                    rate=int(self.RateInput.text())
                )
                session.add(new_partner)

            # Сохраняем изменения в базе данных.
            session.commit()
            QMessageBox.information(self, "Успешно", "Партнёр сохранён!")
            self.go_to_partners_page()
        except Exception as e:
            # Отображаем сообщение об ошибке.
            QMessageBox.critical(self, "Ошибка", str(e))