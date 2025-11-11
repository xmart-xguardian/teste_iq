# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_XGuardian(object):
    def setupUi(self, XGuardian):
        if not XGuardian.objectName():
            XGuardian.setObjectName(u"XGuardian")
        XGuardian.resize(808, 407)
        icon = QIcon()
        icon.addFile(u"xguardian_ico.ico", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        XGuardian.setWindowIcon(icon)
        XGuardian.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(XGuardian)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -70, 821, 671))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label.setPixmap(QPixmap(u"mulher_ti.jpg"))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label_2 = QLabel(XGuardian)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 30, 171, 151))
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2.setPixmap(QPixmap(u"../Downloads/LogoNova-15344c19-removebg-preview.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label_2.setWordWrap(False)
        self.groupBox = QGroupBox(XGuardian)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(240, 200, 321, 161))
        self.groupBox.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"font: 13pt \"Verdana\";")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 100, 161, 21))
        self.lineEdit_2.setStyleSheet(u"border: 1px solid #4d277a;\n"
"border-radius: 3px;")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 80, 58, 16))
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font: 13pt \"Verdana\";")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 30, 58, 16))
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font: 13pt \"Verdana\";")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 71, 101, 31))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 12px; \n"
"    color: blacke;             \n"
"    padding: 6px 16px;       \n"
"	border: 1px solid #4d277a;\n"
"}")
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoRepeat(False)
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 50, 161, 21))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid #4d277a;\n"
"border-radius: 3px;\n"
"\n"
"}")
        self.label_spinner = QLabel(self.groupBox)
        self.label_spinner.setObjectName(u"label_spinner")
        self.label_spinner.setGeometry(QRect(190, 20, 121, 51))
        self.label_spinner.setStyleSheet(u"border-radius: 3px;")
        self.label_spinner.setPixmap(QPixmap(u"spinner.gif"))

        self.retranslateUi(XGuardian)

        QMetaObject.connectSlotsByName(XGuardian)
    # setupUi

    def retranslateUi(self, XGuardian):
        XGuardian.setWindowTitle(QCoreApplication.translate("XGuardian", u"XGuardian Admin", None))
        self.label.setText("")
        self.label_2.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("XGuardian", u"Login", None))
        self.lineEdit_2.setText(QCoreApplication.translate("XGuardian", u"adad", None))
        self.label_3.setText(QCoreApplication.translate("XGuardian", u"Senha", None))
        self.label_4.setText(QCoreApplication.translate("XGuardian", u"Email", None))
        self.pushButton.setText(QCoreApplication.translate("XGuardian", u"Entrar", None))
        self.label_spinner.setText("")
    # retranslateUi

