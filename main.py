from src.classes import *
from PyQt5 import QtWidgets, QtCore, QtGui
from get_ready import Ui_MainWindow
from doc_add_window_dialog import Ui_Dialog  # импорт нашего сгенерированного файла
import sys
import re

if __name__ == '__main__':
    doclist: List[Doctor] = list()


    class mywindow(QtWidgets.QMainWindow):
        def __init__(self):
            super(mywindow, self).__init__()
            self.doc_window = None
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.add_doc)
            self.ui.DoctableWidget.setSortingEnabled(0)  # bugs
            self.ui.DoctableWidget.itemDoubleClicked.connect(self.changeDocs)
            self.ui.delButtonDoc.clicked.connect(self.deleteDoctor)

        def deleteDoctor(self):
            indexes = self.ui.DoctableWidget.selectionModel().selectedRows()
            if len(indexes) > 0:
                for index in indexes:
                    row = index.row()
                    doc_id = list()
                    for i in range(2):
                        doc_id.append(self.ui.DoctableWidget.item(row, i).text())
                    for i in range(len(doclist)):
                        if doc_id[0] == doclist[i].name and doc_id[1] == doclist[i].spec:
                            del doclist[i]
                            break
                self.updateTable()

        def add_doc(self):
            self.create_new_window_doc()
            self.updateTable()

        def updateTable(self):

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
                    self.ui.DoctableWidget.item(i, j).setTextAlignment(
                        QtCore.Qt.AlignHCenter)  # align ! get Nontype somehow(sorting)
                    self.ui.DoctableWidget.item(i, j).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        def changeDocs(self):
            row: int = self.ui.DoctableWidget.currentRow()
            doc_id = list()
            for i in range(2):
                doc_id.append(self.ui.DoctableWidget.item(row, i).text())
            changedDoc = None
            for i in range(len(doclist)):
                if doc_id[0] == doclist[i].name and doc_id[1] == doclist[i].spec:
                    changedDoc = i

            self.create_new_window_doc(changedDoc)
            self.updateTable()

        def create_new_window_doc(self, mode=-1):
            self.doc_window = mywindow1(mode)
            self.doc_window.exec_()


    class mywindow1(QtWidgets.QDialog):
        def __init__(self, mode):
            super(mywindow1, self).__init__()
            self.ui = Ui_Dialog()
            self.ui.setupUi(self)
            self.ui.CabEdit.setValidator(QtGui.QIntValidator())
            self.ui.buttonBox.buttons()[1].clicked.connect(self.close)  # cancel shut down window
            if mode != -1:
                self.ui.buttonBox.buttons()[0].clicked.connect(lambda: self.accept_doc(mode))
                self.show_doc(mode)
            else:
                self.ui.buttonBox.buttons()[0].clicked.connect(self.add_doc)

        def read_doc(self, change_doc = None) -> Optional[Doctor]:
            newDoc = Doctor(self.ui.SpecEdit.displayText(), self.ui.NameEdit.displayText(),
                            int(self.ui.CabEdit.displayText()))
            try:
                for i in doclist:
                    if i.name == newDoc.name and i.spec == newDoc.spec and i != change_doc:
                        raise Exception("Такой доктор уже существует!")

                day_list = list()
                time_list = list()
                for i in self.ui.groupBox.children():
                    if type(i) is QtWidgets.QCheckBox and i.isChecked():
                        day_list.append(i.text())

                    if type(i) is QtWidgets.QLineEdit and i.isEnabled():
                        if re.match(r'[\d]?\d[. ,]\d\d[ ]*[-][ ]*[\d]?\d[. ,]\d\d', i.displayText()):  # check string
                            time_list.append(i.displayText())
                        else:
                            raise Exception("Неправильно введено время работы врача")

                for i in range(len(day_list)):
                    tp = tuple([float(k) for k in time_list[i].replace(",", ".").split("-")])
                    if tp[0] >= tp[1] or tp[0] > 23.59 or tp[1] > 23.59:  # check what time is valid
                        raise Exception("Неправильно введено время работы врача")
                    t_per = Period(tp[0], tp[1])
                    for t in doclist:
                        if t.cabinet == newDoc.cabinet and t.timetable[day_list[i]] \
                                and t.timetable[day_list[i]].is_collision(t_per) and t != change_doc:
                            raise Exception(
                                "Доктор: {0} со специализацией {1} уже работает в этом кабинете в это время".format(
                                    str(t.name), t.spec))
                    newDoc.add_work(day_list[i], t_per)

            except Exception as e:
                msg = QtWidgets.QMessageBox()
                msg.setStyleSheet("QLabel{min-width: 75px;}")
                msg.setStyleSheet("QLabel{min-height: 70px;}")
                msg.setStyleSheet("QString{text-align: left;}")
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText(e.args[0])
                msg.setWindowTitle("Ошибка")
                msg.exec()
                newDoc = None

            return newDoc

        def add_doc(self):
            #     check period collision
            t = self.read_doc()
            if t:
                doclist.append(t)
                self.close()

        def show_doc(self, changedDoc):
            self.ui.SpecEdit.setText(doclist[changedDoc].spec)
            self.ui.NameEdit.setText(doclist[changedDoc].name)
            self.ui.CabEdit.setText(str(doclist[changedDoc].cabinet))
            t: List[str] = list()
            for i in doclist[changedDoc].timetable.keys():
                if doclist[changedDoc].timetable[i]:
                    t.append(i)

            for k in t:
                for i in self.ui.groupBox.children():
                    if type(i) is QtWidgets.QCheckBox and i.text() == k:  # if needed checkbox
                        i.setChecked(1)  # setChecked
                        self.ui.groupBox.findChild(QtWidgets.QLineEdit,  # and add time to matching lineEdit
                                                   "timeEdit_" + i.objectName()[-1]). \
                            setText(str(doclist[changedDoc].timetable[k]))
                        break

        def accept_doc(self, changedDoc):
            d = self.read_doc(doclist[changedDoc])
            if d:
                doclist[changedDoc].change_data(d)
                self.close()


    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
