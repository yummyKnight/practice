# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_ready.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 1181, 581))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(40, 16))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setObjectName("tabWidget")
        self.doc_page = QtWidgets.QWidget()
        self.doc_page.setObjectName("doc_page")
        self.DoctableWidget = QtWidgets.QTableWidget(self.doc_page)
        self.DoctableWidget.setGeometry(QtCore.QRect(10, 20, 1091, 481))
        self.DoctableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DoctableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.DoctableWidget.setShowGrid(True)
        self.DoctableWidget.setObjectName("DoctableWidget")
        self.DoctableWidget.setColumnCount(8)
        self.DoctableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DoctableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DoctableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.DoctableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.DoctableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.DoctableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.DoctableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.DoctableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.DoctableWidget.setHorizontalHeaderItem(7, item)
        self.DoctableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.pushButton = QtWidgets.QPushButton(self.doc_page)
        self.pushButton.setGeometry(QtCore.QRect(1030, 510, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.delButtonDoc = QtWidgets.QPushButton(self.doc_page)
        self.delButtonDoc.setEnabled(True)
        self.delButtonDoc.setGeometry(QtCore.QRect(920, 510, 80, 25))
        self.delButtonDoc.setObjectName("delButtonDoc")
        self.tabWidget.addTab(self.doc_page, "")
        self.patient_page = QtWidgets.QWidget()
        self.patient_page.setObjectName("patient_page")
        self.PattableWidget = QtWidgets.QTableWidget(self.patient_page)
        self.PattableWidget.setGeometry(QtCore.QRect(10, 20, 541, 481))
        self.PattableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PattableWidget.setShowGrid(True)
        self.PattableWidget.setObjectName("PattableWidget")
        self.PattableWidget.setColumnCount(2)
        self.PattableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.PattableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PattableWidget.setHorizontalHeaderItem(1, item)
        self.PattableWidget.horizontalHeader().setDefaultSectionSize(270)
        self.PattableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.DistableWidget = QtWidgets.QTableWidget(self.patient_page)
        self.DistableWidget.setGeometry(QtCore.QRect(610, 20, 531, 481))
        self.DistableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DistableWidget.setShowGrid(True)
        self.DistableWidget.setObjectName("DistableWidget")
        self.DistableWidget.setColumnCount(2)
        self.DistableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.DistableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.DistableWidget.setHorizontalHeaderItem(1, item)
        self.DistableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.pushButton_2 = QtWidgets.QPushButton(self.patient_page)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 520, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.delButtonPat = QtWidgets.QPushButton(self.patient_page)
        self.delButtonPat.setEnabled(True)
        self.delButtonPat.setGeometry(QtCore.QRect(370, 520, 80, 25))
        self.delButtonPat.setObjectName("delButtonPat")
        self.tabWidget.addTab(self.patient_page, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1213, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DoctableWidget.setSortingEnabled(True)
        item = self.DoctableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.DoctableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Специализация"))
        item = self.DoctableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Кабинет"))
        item = self.DoctableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ПН"))
        item = self.DoctableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ВТ"))
        item = self.DoctableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "СР"))
        item = self.DoctableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "ЧТ"))
        item = self.DoctableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "ПТ"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.delButtonDoc.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.doc_page), _translate("MainWindow", "Врачи"))
        self.PattableWidget.setSortingEnabled(True)
        item = self.PattableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.PattableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Болезнь"))
        self.DistableWidget.setSortingEnabled(True)
        item = self.DistableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Болезнь"))
        item = self.DistableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Количество"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить"))
        self.delButtonPat.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patient_page), _translate("MainWindow", "Пациенты"))