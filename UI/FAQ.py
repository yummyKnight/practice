# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\FAQ.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Reference(object):
    def setupUi(self, Reference):
        Reference.setObjectName("Reference")
        Reference.resize(602, 300)
        self.textBrowser = QtWidgets.QTextBrowser(Reference)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 581, 271))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Reference)
        QtCore.QMetaObject.connectSlotsByName(Reference)

    def retranslateUi(self, Reference):
        _translate = QtCore.QCoreApplication.translate
        Reference.setWindowTitle(_translate("Reference", "Справка"))
        self.textBrowser.setHtml(_translate("Reference", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Как пользоваться программой:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1)Добавить пациента/доктора можно с помощью кнопки добавить</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2)Чтобы удалить пацинета или больного нужно выделить строки и нажать кнопку удалить</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3)Двойной клик на любой ячеке открывает меню редкатирования соответствующего доктора/ пациента</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">4) Не может быть пациентов с одинаковыми ФИО, не может быть докторов с одинаковыми ФИО </span><span style=\" font-size:10pt; font-weight:600;\">и</span><span style=\" font-size:10pt;\"> специальностями (то есть могут  быть доктора с одинаковыми ФИО, но разными специальностями)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Исходный код работы: </span><a href=\"https://github.com/yummyKnight/practice\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">https://github.com/yummyKnight/practice</span></a></p></body></html>"))

