from src.classes import *
from PyQt5 import QtWidgets, QtCore
from get_ready import Ui_MainWindow
from doc_window import Ui_DocWindow  # импорт нашего сгенерированного файла
import sys

if __name__ == '__main__':
    doclist: List[Doctor] = list()


    class mywindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(mywindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.doc_window = QtWidgets.QMainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.show_doc_window)

        def show_doc_window(self):
            self.ui = Ui_DocWindow()
            self.ui.setupUi(self.doc_window)
            self.doc_window.show()
            self.ui.buttonBox.buttons()[1].clicked.connect(self.doc_window.close)  # cancel shut down window
            self.ui.buttonBox.buttons()[0].clicked.connect(self.add_doc)

        def add_doc(self):
            self.ui: Ui_DocWindow
            newDoc = Doctor(self.ui.SpecEdit.displayText(), self.ui.NameEdit.displayText(),
                            int(self.ui.CabEdit.displayText()))
            day_list = list()
            time_list = list()
            # day_list.append(self.ui.checkBox_1)
            # day_list.append(self.ui.checkBox_2)
            # day_list.append(self.ui.checkBox_3)
            # day_list.append(self.ui.checkBox_4)
            # day_list.append(self.ui.checkBox_5)
            # time_list.append(self.ui.timeEdit_1)
            # time_list.append(self.ui.timeEdit_2)
            # time_list.append(self.ui.timeEdit_3)
            # time_list.append(self.ui.timeEdit_4)
            # time_list.append(self.ui.timeEdit_5)

            for i in self.ui.groupbox.children():
                if type(i) is QtWidgets.QCheckBox and i.isChecked():
                    day_list.append(i.text())
            for i in self.ui.groupbox.children():
                if type(i) is QtWidgets.QLineEdit and i.isEnabled():
                    time_list.append(i.displayText())

            for i in range(len(day_list)):
                tp = tuple([float(i) for i in time_list[i].replace(",", ".").split("-")])
                newDoc.add_work(day_list[i], Period(tp[0], tp[1]))
            doclist.append(newDoc)
            self.doc_window.close()
            self.updateTable()
            # time_list = [ i for i in [self.ui.docForm.indexOf()]]
            # for i in day_list:
            #     if i.isChecked():
            #         days.append(i.text())
            # tp = tuple([float(i) for i in self.ui..displayText().replace(",", ".").split("-")])

        # def butClicked(self):
        #     newDoc = Doctor(self.ui.lineEdit_2.displayText(), self.ui.lineEdit.displayText())
        #     days = list()
        #     self.ui.checkBox.setParent(self.ui.groupBox)
        #     self.ui.checkBox_2.setParent(self.ui.groupBox)
        #     self.ui.checkBox_3.setParent(self.ui.groupBox)
        #     self.ui.checkBox_4.setParent(self.ui.groupBox)
        #     self.ui.checkBox_5.setParent(self.ui.groupBox)
        #     self.ui.checkBox_6.setParent(self.ui.groupBox)
        #     buttonList : List[QtWidgets.QCheckBox] = self.ui.groupBox.children()
        #     for i in buttonList:
        #         if i.objectName().find("checkBox") != -1 and i.isChecked():
        #             days.append(i.text())
        #     tp = tuple([float(i) for i in self.ui.lineEdit_4.displayText().replace(",", ".").split("-")])
        #     newDoc.add_work(self.ui.lineEdit_3.displayText(), days, Period(tp[0], tp[1]))
        #     doclist.append(newDoc)
        #

        def updateTable(self):
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.show_doc_window)
            self.ui.DoctableWidget.clearContents()
            self.ui.DoctableWidget.setRowCount(len(doclist))
            for i in range(self.ui.DoctableWidget.rowCount()):
                for j in range(self.ui.DoctableWidget.columnCount()):
                    self.ui.DoctableWidget.item(i, j).setTextAlignment(QtCore.Qt.AlignHCenter)

            row = 0
            for doc in doclist:
                col = 0
                self.ui.DoctableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(doc.name))
                col += 1
                self.ui.DoctableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(doc.spec))
                col += 1
                # get cab values
                self.ui.DoctableWidget.setItem(row, col,  QtWidgets.QTableWidgetItem(str(doc.cabinet)))
                col += 1
                # get time values
                for i in Schedule.week:
                    k = str(doc.timetable[i])
                    if k == "None":
                        k = "-"
                    self.ui.DoctableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(k))
                    col += 1
                row += 1


    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
    # Patient1 = Patient("Vasya Petrov")
    # inp = "Vertaynka"
    # Patient1.add_disease(inp)
    # Patient2 = Patient("Varvara Ilyana")
    # Patient2.add_disease(inp)
    # print(Patient.g_diseases)
