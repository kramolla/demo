# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_PartnerList(object):
    def setupUi(self, PartnerList):
        if not PartnerList.objectName():
            PartnerList.setObjectName(u"PartnerList")
        PartnerList.resize(800, 600)
        self.verticalLayout_2 = QVBoxLayout(PartnerList)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout.setContentsMargins(280, -1, 280, -1)
        self.label = QLabel(PartnerList)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setPixmap(QPixmap(u"../icons/Master_pol.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(PartnerList)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 16777215))
        font = QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(PartnerList)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.layout = QWidget()
        self.layout.setObjectName(u"layout")
        self.layout.setGeometry(QRect(0, 0, 780, 450))
        self.verticalLayoutWidget = QWidget(self.layout)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 781, 471))
        self.list = QVBoxLayout(self.verticalLayoutWidget)
        self.list.setObjectName(u"list")
        self.list.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.layout)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.addPartnerButton = QPushButton(PartnerList)
        self.addPartnerButton.setObjectName(u"addPartnerButton")
        self.addPartnerButton.setStyleSheet(u"background-color: #67BA80; border: none")

        self.verticalLayout_2.addWidget(self.addPartnerButton)


        self.retranslateUi(PartnerList)

        QMetaObject.connectSlotsByName(PartnerList)
    # setupUi

    def retranslateUi(self, PartnerList):
        PartnerList.setWindowTitle(QCoreApplication.translate("PartnerList", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("PartnerList", u"\u041f\u0430\u0440\u0442\u043d\u0451\u0440\u044b", None))
        self.addPartnerButton.setText(QCoreApplication.translate("PartnerList", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u0440\u0442\u043d\u0451\u0440\u0430", None))
    # retranslateUi

