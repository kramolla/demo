# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ordercard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_OrderCard(object):
    def setupUi(self, OrderCard):
        if not OrderCard.objectName():
            OrderCard.setObjectName(u"OrderCard")
        OrderCard.resize(800, 130)
        OrderCard.setStyleSheet(u"background-color: #fff; color: #000; font-size: 18px; border: 2px solid black")
        self.verticalLayout = QVBoxLayout(OrderCard)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.product_name = QLabel(OrderCard)
        self.product_name.setObjectName(u"product_name")
        self.product_name.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.product_name)

        self.quantity_of_products = QLabel(OrderCard)
        self.quantity_of_products.setObjectName(u"quantity_of_products")
        self.quantity_of_products.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.quantity_of_products)

        self.date_of_create = QLabel(OrderCard)
        self.date_of_create.setObjectName(u"date_of_create")
        self.date_of_create.setStyleSheet(u"border: none")

        self.verticalLayout.addWidget(self.date_of_create)


        self.retranslateUi(OrderCard)

        QMetaObject.connectSlotsByName(OrderCard)
    # setupUi

    def retranslateUi(self, OrderCard):
        OrderCard.setWindowTitle(QCoreApplication.translate("OrderCard", u"Form", None))
        self.product_name.setText(QCoreApplication.translate("OrderCard", u"product_name", None))
        self.quantity_of_products.setText(QCoreApplication.translate("OrderCard", u"quantity_of_products", None))
        self.date_of_create.setText(QCoreApplication.translate("OrderCard", u"date_of_create", None))
    # retranslateUi

