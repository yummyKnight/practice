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
            self.doc_window = QtWidgets.QMainWindow()
            self.setupMainWindow()

        def setupMainWindow(self):
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.show_doc_window)
            self.ui.DoctableWidget.itemDoubleClicked.connect(self.changeDocs)

        def show_doc_window(self):  # 0 - add mode, 1 - correction mode
            self.ui = Ui_DocWindow()
            self.ui.setupUi(self.doc_window)
            self.doc_window.show()
            self.ui.buttonBox.buttons()[1].clicked.connect(self.doc_window.close)  # cancel shut down window
            self.ui.buttonBox.buttons()[0].clicked.connect(self.add_doc)

        def read_doc(self) -> Doctor:
            self.ui: Ui_DocWindow
            newDoc = Doctor(self.ui.SpecEdit.displayText(), self.ui.NameEdit.displayText(),
                            int(self.ui.CabEdit.displayText()))
            day_list = list()
            time_list = list()

            for i in self.ui.groupbox.children():
                if type(i) is QtWidgets.QCheckBox and i.isChecked():
                    day_list.append(i.text())
                if type(i) is QtWidgets.QLineEdit and i.isEnabled():
                    time_list.append(i.displayText())

            for i in range(len(day_list)):
                tp = tuple([float(i) for i in time_list[i].replace(",", ".").split("-")])
                newDoc.add_work(day_list[i], Period(tp[0], tp[1]))

            return newDoc

        def add_doc(self):

            #     check period collision
            doclist.append(self.read_doc())
            self.doc_window.close()
            self.updateTable()

        def updateTable(self):
            self.setupMainWindow()
            self.ui: Ui_MainWindow  # static analizer command

            self.ui.DoctableWidget.clearContents()
            self.ui.DoctableWidget.setRowCount(len(doclist))

            row = 0
            for doc in doclist:
                col = 0
                self.ui.DoctableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(doc.name))
                col += 1
                self.ui.DoctableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(doc.spec))
                col += 1
                # get cab values
                self.ui.DoctableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(doc.cabinet)))
                col += 1
                # get time values
                for i in Schedule.week:
                    k = str(doc.timetable[i])
                    if k == "None":
                        k = "-"
                    self.ui.DoctableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(k))
                    col += 1
                row += 1

            for i in range(self.ui.DoctableWidget.rowCount()):
                for j in range(self.ui.DoctableWidget.columnCount()):
                    self.ui.DoctableWidget.item(i, j).setTextAlignment(QtCore.Qt.AlignHCenter)  # align
                    self.ui.DoctableWidget.item(i, j).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        def changeDocs(self):
            self.ui: Ui_MainWindow
            row: int = self.ui.DoctableWidget.currentRow()
            doc_id = list()
            for i in range(2):
                doc_id.append(self.ui.DoctableWidget.item(row, i).text())
            changedDoc = None
            for i in range(len(doclist)):
                if doc_id[0] == doclist[i].name and doc_id[1] == doclist[i].spec:
                    changedDoc = i
            self.show_doc_window()
            self.ui: Ui_DocWindow
            self.ui.buttonBox.buttons()[0].clicked.connect(self.change_doc)
            self.ui.SpecEdit.setText(doclist[changedDoc].spec)
            self.ui.NameEdit.setText(doclist[changedDoc].name)
            self.ui.CabEdit.setText(str(doclist[changedDoc].cabinet))
            t: List[str] = list()
            for i in doclist[changedDoc].timetable.keys():
                if doclist[changedDoc].timetable[i]:
                    t.append(i)

            for k in t:
                for i in self.ui.groupbox.children():
                    if type(i) is QtWidgets.QCheckBox and i.text() == k:  # if needed checkbox
                        i.setChecked(1)  # setChecked
                        self.ui.groupbox.findChild(QtWidgets.QLineEdit,  # and add time to matching lineEdit
                                                   "timeEdit_" + i.objectName()[-1]). \
                            setText(str(doclist[changedDoc].timetable[k]))
                        break

        def change_doc(self, doc_num: int):

            doclist[doc_num].change_data(self.read_doc())
            self.doc_window.close()
            self.updateTable()

    class mywindow1(QtWidgets.QMainWindow):
        def __init__(self):
            super(mywindow1, self).__init__()
            self.ui = Ui_DocWindow()
            self.ui.setupUi(self)
            self.ui.buttonBox.buttons()[1].clicked.connect(self.close)  # cancel shut down window
            self.ui.buttonBox.buttons()[0].clicked.connect(self.add_doc)

    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
