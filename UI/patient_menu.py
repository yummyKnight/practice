# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'patient_menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PatientD(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBoxPatient = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBoxPatient.setGeometry(QtCore.QRect(50, 250, 321, 32))
        self.buttonBoxPatient.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.buttonBoxPatient.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxPatient.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxPatient.setObjectName("buttonBoxPatient")
        self.PatientEdit = QtWidgets.QLineEdit(Dialog)
        self.PatientEdit.setGeometry(QtCore.QRect(50, 80, 311, 25))
        self.PatientEdit.setObjectName("PatientEdit")
        self.DisEdit = QtWidgets.QLineEdit(Dialog)
        self.DisEdit.setGeometry(QtCore.QRect(50, 160, 321, 71))
        self.DisEdit.setObjectName("DisEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 321, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBoxPatient.accepted.connect(Dialog.accept)
        self.buttonBoxPatient.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ФИО"))
        self.label_2.setText(_translate("Dialog", "Заболевания"))
