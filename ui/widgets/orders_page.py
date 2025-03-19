# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orderspage.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_OrdersPage(object):
    def setupUi(self, OrdersPage):
        if not OrdersPage.objectName():
            OrdersPage.setObjectName(u"OrdersPage")
        OrdersPage.resize(619, 447)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OrdersPage.sizePolicy().hasHeightForWidth())
        OrdersPage.setSizePolicy(sizePolicy)
        OrdersPage.setStyleSheet(u"background-color: #fff;\n"
"font-size: 18px\n"
"")
        self.verticalLayout = QVBoxLayout(OrdersPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title = QLabel(OrdersPage)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"color: black; font-size: 20px")

        self.verticalLayout.addWidget(self.Title)

        self.scrollArea = QScrollArea(OrdersPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 599, 364))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.list = QVBoxLayout()
        self.list.setObjectName(u"list")

        self.verticalLayout_4.addLayout(self.list)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.BackButton = QPushButton(OrdersPage)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.BackButton.setStyleSheet(u"background: #67BA80;\n"
"border: none;")

        self.verticalLayout.addWidget(self.BackButton)


        self.retranslateUi(OrdersPage)

        QMetaObject.connectSlotsByName(OrdersPage)
    # setupUi

    def retranslateUi(self, OrdersPage):
        OrdersPage.setWindowTitle(QCoreApplication.translate("OrdersPage", u"Form", None))
        self.Title.setText(QCoreApplication.translate("OrdersPage", u"<html><head/><body><p align=\"center\">\u0417\u0430\u043a\u0430\u0437\u044b</p></body></html>", None))
        self.BackButton.setText(QCoreApplication.translate("OrdersPage", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

