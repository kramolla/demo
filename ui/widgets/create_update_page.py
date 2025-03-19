# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createupdatepage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CreateUpdatePage(object):
    def setupUi(self, CreateUpdatePage):
        if not CreateUpdatePage.objectName():
            CreateUpdatePage.setObjectName(u"CreateUpdatePage")
        CreateUpdatePage.resize(582, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateUpdatePage.sizePolicy().hasHeightForWidth())
        CreateUpdatePage.setSizePolicy(sizePolicy)
        CreateUpdatePage.setStyleSheet(u".QPushButton{\n"
"	background-color: #67BA80;\n"
"	border: none\n"
"}\n"
"\n"
"QWidget{\n"
"	font-size: 18px\n"
"}")
        self.verticalLayout = QVBoxLayout(CreateUpdatePage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(CreateUpdatePage)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.TypeInput = QComboBox(CreateUpdatePage)
        self.TypeInput.addItem("")
        self.TypeInput.addItem("")
        self.TypeInput.addItem("")
        self.TypeInput.addItem("")
        self.TypeInput.setObjectName(u"TypeInput")
        self.TypeInput.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.TypeInput)

        self.label_2 = QLabel(CreateUpdatePage)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.NameInput = QLineEdit(CreateUpdatePage)
        self.NameInput.setObjectName(u"NameInput")

        self.verticalLayout.addWidget(self.NameInput)

        self.label_3 = QLabel(CreateUpdatePage)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.BossNameInput = QLineEdit(CreateUpdatePage)
        self.BossNameInput.setObjectName(u"BossNameInput")

        self.verticalLayout.addWidget(self.BossNameInput)

        self.label_4 = QLabel(CreateUpdatePage)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.EmailInput = QLineEdit(CreateUpdatePage)
        self.EmailInput.setObjectName(u"EmailInput")

        self.verticalLayout.addWidget(self.EmailInput)

        self.label_5 = QLabel(CreateUpdatePage)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.PhoneNumberInput = QLineEdit(CreateUpdatePage)
        self.PhoneNumberInput.setObjectName(u"PhoneNumberInput")

        self.verticalLayout.addWidget(self.PhoneNumberInput)

        self.label_6 = QLabel(CreateUpdatePage)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.AddressInput = QLineEdit(CreateUpdatePage)
        self.AddressInput.setObjectName(u"AddressInput")

        self.verticalLayout.addWidget(self.AddressInput)

        self.label_7 = QLabel(CreateUpdatePage)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.InnInput = QLineEdit(CreateUpdatePage)
        self.InnInput.setObjectName(u"InnInput")

        self.verticalLayout.addWidget(self.InnInput)

        self.label_8 = QLabel(CreateUpdatePage)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.RateInput = QLineEdit(CreateUpdatePage)
        self.RateInput.setObjectName(u"RateInput")

        self.verticalLayout.addWidget(self.RateInput)

        self.SaveButton = QPushButton(CreateUpdatePage)
        self.SaveButton.setObjectName(u"SaveButton")
        self.SaveButton.setMinimumSize(QSize(0, 0))
        self.SaveButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.SaveButton)

        self.CancelButton = QPushButton(CreateUpdatePage)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.CancelButton)


        self.retranslateUi(CreateUpdatePage)

        QMetaObject.connectSlotsByName(CreateUpdatePage)
    # setupUi

    def retranslateUi(self, CreateUpdatePage):
        CreateUpdatePage.setWindowTitle(QCoreApplication.translate("CreateUpdatePage", u"Form", None))
        self.label.setText(QCoreApplication.translate("CreateUpdatePage", u"\u0422\u0438\u043f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.TypeInput.setItemText(0, QCoreApplication.translate("CreateUpdatePage", u"\u041e\u041e\u041e", None))
        self.TypeInput.setItemText(1, QCoreApplication.translate("CreateUpdatePage", u"\u041e\u0410\u041e", None))
        self.TypeInput.setItemText(2, QCoreApplication.translate("CreateUpdatePage", u"\u0417\u0410\u041e", None))
        self.TypeInput.setItemText(3, QCoreApplication.translate("CreateUpdatePage", u"\u041f\u0410\u041e", None))

        self.label_2.setText(QCoreApplication.translate("CreateUpdatePage", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u043c\u043f\u0430\u043d\u0438\u0438", None))
        self.label_3.setText(QCoreApplication.translate("CreateUpdatePage", u"\u0418\u043c\u044f \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0430", None))
        self.label_4.setText(QCoreApplication.translate("CreateUpdatePage", u"\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043e\u0447\u0442\u0430", None))
        self.label_5.setText(QCoreApplication.translate("CreateUpdatePage", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.PhoneNumberInput.setInputMask(QCoreApplication.translate("CreateUpdatePage", u"999 999 99 99", None))
        self.label_6.setText(QCoreApplication.translate("CreateUpdatePage", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.label_7.setText(QCoreApplication.translate("CreateUpdatePage", u"\u0418\u041d\u041d", None))
        self.InnInput.setInputMask(QCoreApplication.translate("CreateUpdatePage", u"9999999999", None))
        self.label_8.setText(QCoreApplication.translate("CreateUpdatePage", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433", None))
        self.SaveButton.setText(QCoreApplication.translate("CreateUpdatePage", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.CancelButton.setText(QCoreApplication.translate("CreateUpdatePage", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

