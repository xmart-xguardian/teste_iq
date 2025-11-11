# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'after_login.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(803, 419)
        icon = QIcon()
        icon.addFile(u"xguardian_ico.ico", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(260, 10, 531, 411))
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(77, 39, 122);")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 340, 121, 61))
        self.widget.setStyleSheet(u" background-color: white;\n"
" border-radius: 3px;")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 30, 75, 24))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.pushButton_2.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(77, 39, 122);")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 121, 16))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";\n"
"background-color: rgb(77, 39, 122);\n"
"border-radius: 0px;\n"
"")
        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 30, 511, 181))
        self.widget_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 3px;")
        self.comboBox = QComboBox(self.widget_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 30, 311, 41))
        self.comboBox.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #fff;\n"
"    color: #222;\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 6px;\n"
"    padding: 4px 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background: #fff;\n"
"    border-left: 1px solid #bbb;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/down_arrow_black.png); /* use um \u00edcone preto, ou remova esta linha */\n"
"    width: 14px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #fff;\n"
"    color: #222;\n"
"    selection-background-color: #eee;\n"
"    selection-color: #111;\n"
"    border: none;\n"
"}")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 90, 121, 31))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #fff;\n"
"    color: #222;\n"
"    border: 1px solid #bbb;\n"
"    border-radius: 6px;\n"
"    padding: 6px 16px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #eee;\n"
"    border: 1px solid #999;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ddd;\n"
"}")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 511, 21))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 12pt \"Segoe UI\";\n"
"background-color: rgb(77, 39, 122);\n"
"border-radius: 0px;")
        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(400, 340, 121, 61))
        self.widget_3.setStyleSheet(u" background-color: white;\n"
" border-radius: 3px;")
        self.pushButton_4 = QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 30, 75, 24))
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.pushButton_4.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(77, 39, 122);")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 121, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 900 9pt \"Segoe UI\";\n"
"background-color: rgb(77, 39, 122);\n"
"border-radius: 0px;\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 90, 241, 241))
        self.label.setMinimumSize(QSize(100, 100))
        self.label.setMaximumSize(QSize(16777, 16777))
        self.label.setStyleSheet(u"")
        self.label.setScaledContents(False)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(80, 390, 101, 21))
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(77, 39, 122);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 3px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Menu Principal", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Painel", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Ligar", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"BANCO DEV", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Organiza\u00e7\u00f5es", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Ativar", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Rob\u00f4 Testes", None))
        self.label.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"SAIR", None))
    # retranslateUi

