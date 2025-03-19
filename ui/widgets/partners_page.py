# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'partnerspage.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_PartnersPage(object):
    def setupUi(self, PartnersPage):
        if not PartnersPage.objectName():
            PartnersPage.setObjectName(u"PartnersPage")
        PartnersPage.resize(1000, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PartnersPage.sizePolicy().hasHeightForWidth())
        PartnersPage.setSizePolicy(sizePolicy)
        PartnersPage.setMinimumSize(QSize(0, 0))
        PartnersPage.setAutoFillBackground(False)
        PartnersPage.setStyleSheet(u"QWidget{background: white;\n"
"font-size: 18px}")
        self.verticalLayout_2 = QVBoxLayout(PartnersPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalWidget = QWidget(PartnersPage)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalWidget = QWidget(self.verticalWidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy1)
        self.horizontalWidget.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(1, -1, 1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.horizontalWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 100))
        self.label_3.setPixmap(QPixmap(u"../icons/Master_pol.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.horizontalWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.horizontalWidget)

        self.scrollArea = QScrollArea(self.verticalWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 962, 320))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_3.addWidget(self.listWidget)

        self.list = QVBoxLayout()
        self.list.setObjectName(u"list")

        self.verticalLayout_3.addLayout(self.list)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.addPartnerButton = QPushButton(self.verticalWidget)
        self.addPartnerButton.setObjectName(u"addPartnerButton")
        self.addPartnerButton.setMinimumSize(QSize(0, 30))
        self.addPartnerButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.addPartnerButton.setStyleSheet(u"background-color: #67BA80; border: none")

        self.verticalLayout.addWidget(self.addPartnerButton)


        self.verticalLayout_2.addWidget(self.verticalWidget)


        self.retranslateUi(PartnersPage)

        QMetaObject.connectSlotsByName(PartnersPage)
    # setupUi

    def retranslateUi(self, PartnersPage):
        PartnersPage.setWindowTitle(QCoreApplication.translate("PartnersPage", u"Form", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("PartnersPage", u"\u041f\u0430\u0440\u0442\u043d\u0451\u0440\u044b", None))
        self.addPartnerButton.setText(QCoreApplication.translate("PartnersPage", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u0440\u0442\u043d\u0451\u0440\u0430", None))
    # retranslateUi

