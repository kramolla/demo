# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'partnercard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_PartnerCard(object):
    def setupUi(self, PartnerCard):
        if not PartnerCard.objectName():
            PartnerCard.setObjectName(u"PartnerCard")
        PartnerCard.resize(900, 202)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PartnerCard.sizePolicy().hasHeightForWidth())
        PartnerCard.setSizePolicy(sizePolicy)
        PartnerCard.setMinimumSize(QSize(0, 0))
        PartnerCard.setStyleSheet(u"font-size: 18px;\n"
"padding: 0px")
        self.horizontalLayout_3 = QHBoxLayout(PartnerCard)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalFrame = QFrame(PartnerCard)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 0))
        self.horizontalFrame.setStyleSheet(u"border: 2px solid black;")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.FirstColumn = QFrame(self.horizontalFrame)
        self.FirstColumn.setObjectName(u"FirstColumn")
        self.FirstColumn.setEnabled(True)
        self.FirstColumn.setStyleSheet(u"border: none; padding: 0;")
        self.verticalLayout = QVBoxLayout(self.FirstColumn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PartnerTypeAndName = QPushButton(self.FirstColumn)
        self.PartnerTypeAndName.setObjectName(u"PartnerTypeAndName")
        self.PartnerTypeAndName.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.PartnerTypeAndName)

        self.BossName = QPushButton(self.FirstColumn)
        self.BossName.setObjectName(u"BossName")
        self.BossName.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.BossName)

        self.PhoneNumber = QPushButton(self.FirstColumn)
        self.PhoneNumber.setObjectName(u"PhoneNumber")
        self.PhoneNumber.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.PhoneNumber)

        self.Rank = QPushButton(self.FirstColumn)
        self.Rank.setObjectName(u"Rank")
        self.Rank.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.Rank)


        self.horizontalLayout_2.addWidget(self.FirstColumn)

        self.DiscountPercentage = QPushButton(self.horizontalFrame)
        self.DiscountPercentage.setObjectName(u"DiscountPercentage")
        self.DiscountPercentage.setMinimumSize(QSize(0, 0))
        self.DiscountPercentage.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.DiscountPercentage.setStyleSheet(u"border: none")

        self.horizontalLayout_2.addWidget(self.DiscountPercentage)


        self.horizontalLayout_3.addWidget(self.horizontalFrame)

        self.GetOrdersListButton = QPushButton(PartnerCard)
        self.GetOrdersListButton.setObjectName(u"GetOrdersListButton")
        self.GetOrdersListButton.setMinimumSize(QSize(0, 180))
        self.GetOrdersListButton.setMaximumSize(QSize(180, 16777215))
        self.GetOrdersListButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.GetOrdersListButton.setStyleSheet(u"background-color: #67BA80;   border-radius: 10px")

        self.horizontalLayout_3.addWidget(self.GetOrdersListButton)


        self.retranslateUi(PartnerCard)

        QMetaObject.connectSlotsByName(PartnerCard)
    # setupUi

    def retranslateUi(self, PartnerCard):
        PartnerCard.setWindowTitle(QCoreApplication.translate("PartnerCard", u"Form", None))
        self.PartnerTypeAndName.setText(QCoreApplication.translate("PartnerCard", u"PushButton", None))
        self.BossName.setText(QCoreApplication.translate("PartnerCard", u"PushButton", None))
        self.PhoneNumber.setText(QCoreApplication.translate("PartnerCard", u"PushButton", None))
        self.Rank.setText(QCoreApplication.translate("PartnerCard", u"PushButton", None))
        self.DiscountPercentage.setText(QCoreApplication.translate("PartnerCard", u"PushButton", None))
        self.GetOrdersListButton.setText(QCoreApplication.translate("PartnerCard", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \n"
" \u0438\u0441\u0442\u043e\u0440\u0438\u044e", None))
    # retranslateUi

