# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editpartnerdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_EditPartnerDialog(object):
    def setupUi(self, EditPartnerDialog):
        if not EditPartnerDialog.objectName():
            EditPartnerDialog.setObjectName(u"EditPartnerDialog")
        EditPartnerDialog.setEnabled(True)
        EditPartnerDialog.resize(400, 300)
        EditPartnerDialog.setMinimumSize(QSize(400, 300))
        EditPartnerDialog.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u"../icons/Master_pol.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        EditPartnerDialog.setWindowIcon(icon)
        EditPartnerDialog.setStyleSheet(u"QPushButton{\n"
"	background-color: #67BA80;\n"
"	border: none\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(EditPartnerDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.type_input = QComboBox(EditPartnerDialog)
        self.type_input.addItem("")
        self.type_input.addItem("")
        self.type_input.addItem("")
        self.type_input.addItem("")
        self.type_input.setObjectName(u"type_input")

        self.verticalLayout_2.addWidget(self.type_input)

        self.name_input = QLineEdit(EditPartnerDialog)
        self.name_input.setObjectName(u"name_input")

        self.verticalLayout_2.addWidget(self.name_input)

        self.boss_name_input = QLineEdit(EditPartnerDialog)
        self.boss_name_input.setObjectName(u"boss_name_input")

        self.verticalLayout_2.addWidget(self.boss_name_input)

        self.email_input = QLineEdit(EditPartnerDialog)
        self.email_input.setObjectName(u"email_input")

        self.verticalLayout_2.addWidget(self.email_input)

        self.phone_number_input = QLineEdit(EditPartnerDialog)
        self.phone_number_input.setObjectName(u"phone_number_input")

        self.verticalLayout_2.addWidget(self.phone_number_input)

        self.address_input = QLineEdit(EditPartnerDialog)
        self.address_input.setObjectName(u"address_input")

        self.verticalLayout_2.addWidget(self.address_input)

        self.inn_input = QLineEdit(EditPartnerDialog)
        self.inn_input.setObjectName(u"inn_input")

        self.verticalLayout_2.addWidget(self.inn_input)

        self.rate_input = QLineEdit(EditPartnerDialog)
        self.rate_input.setObjectName(u"rate_input")

        self.verticalLayout_2.addWidget(self.rate_input)

        self.save_button = QPushButton(EditPartnerDialog)
        self.save_button.setObjectName(u"save_button")

        self.verticalLayout_2.addWidget(self.save_button)

        self.cancel_button = QPushButton(EditPartnerDialog)
        self.cancel_button.setObjectName(u"cancel_button")

        self.verticalLayout_2.addWidget(self.cancel_button)


        self.retranslateUi(EditPartnerDialog)

        QMetaObject.connectSlotsByName(EditPartnerDialog)
    # setupUi

    def retranslateUi(self, EditPartnerDialog):
        EditPartnerDialog.setWindowTitle(QCoreApplication.translate("EditPartnerDialog", u"Dialog", None))
        self.type_input.setItemText(0, QCoreApplication.translate("EditPartnerDialog", u"\u041e\u041e\u041e", None))
        self.type_input.setItemText(1, QCoreApplication.translate("EditPartnerDialog", u"\u041e\u0410\u041e", None))
        self.type_input.setItemText(2, QCoreApplication.translate("EditPartnerDialog", u"\u0417\u0410\u041e", None))
        self.type_input.setItemText(3, QCoreApplication.translate("EditPartnerDialog", u"\u041f\u0410\u041e", None))

        self.save_button.setText(QCoreApplication.translate("EditPartnerDialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancel_button.setText(QCoreApplication.translate("EditPartnerDialog", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

