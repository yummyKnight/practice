from src.classes import *
from PyQt5 import QtWidgets, QtCore, QtGui
from UI.get_ready import Ui_MainWindow
from UI.doc_add_window_dialog import Ui_Dialog
from UI.patient_menu import Ui_PatientD
# импорт нашего сгенерированного файла
import sys
import re

if __name__ == '__main__':
    doc_list: List[Doctor] = list()
    patient_list: List[Patient] = list()


    class MyMainWindow(QtWidgets.QMainWindow):
        def __init__(self) -> None:
            super(MyMainWindow, self).__init__()
            self.doc_window = None
            self.pat_window = None
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.pushButton.clicked.connect(self.add_doc)
            self.ui.pushButton_2.clicked.connect(self.add_patient)
            self.ui.DoctableWidget.setSortingEnabled(0)  # bugs
            self.ui.DoctableWidget.itemDoubleClicked.connect(self.change_doc)
            self.ui.PattableWidget.itemDoubleClicked.connect(self.change_patient)
            self.ui.delButtonDoc.clicked.connect(self.delete_doc)
            self.ui.delButtonPat.clicked.connect(self.delete_patient)

        def delete_doc(self):
            indexes = self.ui.DoctableWidget.selectionModel().selectedRows()
            if len(indexes) > 0:
                for index in indexes:
                    row = index.row()
                    doc_id = list()
                    for i in range(2):
                        doc_id.append(self.ui.DoctableWidget.item(row, i).text())
                    for i in range(len(doc_list)):
                        if doc_id[0] == doc_list[i].name and doc_id[1] == doc_list[i].spec:
                            del doc_list[i]
                            break
                self.update_doc_table()

        def set_immutable(self, tableWidget: QtWidgets.QTableWidget):
            for i in range(tableWidget.rowCount()):
                for j in range(tableWidget.columnCount()):
                    tableWidget.item(i, j).setTextAlignment(
                        QtCore.Qt.AlignHCenter)  # align ! get Nontype somehow(sorting)
                    tableWidget.item(i, j).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

        def add_doc(self):
            self.create_new_window_doc()
            self.update_doc_table()

        def update_doc_table(self):

            self.ui.DoctableWidget.clearContents()
            self.ui.DoctableWidget.setRowCount(len(doc_list))

            row = 0
            for doc in doc_list:
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

            self.set_immutable(self.ui.DoctableWidget)

        def change_doc(self):
            row: int = self.ui.DoctableWidget.currentRow()
            doc_id = list()
            for i in range(2):
                doc_id.append(self.ui.DoctableWidget.item(row, i).text())
            changedDoc = None
            for i in range(len(doc_list)):
                if doc_id[0] == doc_list[i].name and doc_id[1] == doc_list[i].spec:
                    changedDoc = i

            self.create_new_window_doc(changedDoc)
            self.update_doc_table()

        def create_new_window_doc(self, mode=-1):
            self.doc_window = DocWindow(mode)
            self.doc_window.exec_()

        def create_new_window_pat(self, mode=-1):
            self.pat_window = PatientWindow(mode)
            self.pat_window.exec_()

        def update_patient_table(self):

            self.update_dis_table()
            self.ui.PattableWidget.clearContents()
            self.ui.PattableWidget.setRowCount(len(patient_list))
            row = 0
            for pat in patient_list:
                col = 0
                self.ui.PattableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(pat.name))
                col += 1
                self.ui.PattableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(", ".join(pat._diseases)))
                row += 1

            self.set_immutable(self.ui.PattableWidget)

        def update_dis_table(self):
            self.ui.DistableWidget.clearContents()
            self.ui.DistableWidget.setRowCount(len(Patient.g_diseases))
            row = 0
            for dis in Patient.g_diseases.keys():
                col = 0
                self.ui.DistableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(dis))
                col += 1
                self.ui.DistableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(str(Patient.g_diseases[dis])))
                row += 1
            self.set_immutable(self.ui.DistableWidget)
        def add_patient(self):
            self.create_new_window_pat()
            self.update_patient_table()

        def change_patient(self):
            row: int = self.ui.PattableWidget.currentRow()
            pat_id = self.ui.PattableWidget.item(row, 0).text()
            changed_pat = None
            for i in range(len(patient_list)):
                if pat_id == patient_list[i].name:
                    changed_pat = i

            self.create_new_window_pat(changed_pat)
            self.update_patient_table()

        def delete_patient(self):
            indexes = self.ui.PattableWidget.selectionModel().selectedRows()
            if len(indexes) > 0:
                for index in indexes:
                    row = index.row()
                    pat_id = self.ui.PattableWidget.item(row, 0).text()
                    for i in range(len(patient_list)):
                        if pat_id == patient_list[i].name:
                            del patient_list[i]
                            break
                self.update_patient_table()


class DocWindow(QtWidgets.QDialog):
    def __init__(self, mode):
        super(DocWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.CabEdit.setValidator(QtGui.QIntValidator())
        self.ui.buttonBox.buttons()[1].clicked.connect(self.close)  # cancel shut down window
        if mode != -1:
            self.ui.buttonBox.buttons()[0].clicked.connect(lambda: self.accept_doc(mode))
            self.show_doc(mode)
        else:
            self.ui.buttonBox.buttons()[0].clicked.connect(self.add_doc)

    def read_doc(self, change_doc=None) -> Optional[Doctor]:
        newDoc = Doctor(self.ui.SpecEdit.displayText(), self.ui.NameEdit.displayText(),
                        int(self.ui.CabEdit.displayText()))
        try:
            if newDoc.name == "":
                raise Exception("Введите имя врача!")
            if newDoc.spec == "":
                raise Exception("Введите специализацию врача!")
            for i in doc_list:
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
                for t in doc_list:
                    if t.cabinet == newDoc.cabinet and t.timetable[day_list[i]] \
                            and t.timetable[day_list[i]].is_collision(t_per) and t != change_doc:
                        raise Exception(
                            "Доктор: {0} со специализацией {1} уже работает в {2} этом кабинете в это время".format(
                                str(t.name), t.spec, day_list[i]))

                newDoc.add_work(day_list[i], t_per)

        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setStyleSheet("QLabel{min-width: 75cpx;}")
            msg.setStyleSheet("QLabel{min-height: 70px;}")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(e.args[0])
            msg.setWindowTitle("Ошибка")
            msg.exec()
            newDoc = None

        return newDoc

    def add_doc(self):
        t = self.read_doc()
        if t:
            doc_list.append(t)
            self.close()

    def show_doc(self, changedDoc):
        self.ui.SpecEdit.setText(doc_list[changedDoc].spec)
        self.ui.NameEdit.setText(doc_list[changedDoc].name)
        self.ui.CabEdit.setText(str(doc_list[changedDoc].cabinet))
        t: List[str] = list()
        for i in doc_list[changedDoc].timetable.keys():
            if doc_list[changedDoc].timetable[i]:
                t.append(i)

        for k in t:
            for i in self.ui.groupBox.children():
                if type(i) is QtWidgets.QCheckBox and i.text() == k:  # if needed checkbox
                    i.setChecked(1)  # setChecked
                    self.ui.groupBox.findChild(QtWidgets.QLineEdit,  # and add time to matching lineEdit
                                               "timeEdit_" + i.objectName()[-1]). \
                        setText(str(doc_list[changedDoc].timetable[k]))
                    break

    def accept_doc(self, changedDoc):
        d = self.read_doc(doc_list[changedDoc])
        if d:
            doc_list[changedDoc].change_data(d)
            self.close()


class PatientWindow(QtWidgets.QDialog):
    def __init__(self, mode=-1) -> None:
        super(PatientWindow, self).__init__()
        self.ui = Ui_PatientD()
        self.ui.setupUi(self)
        self.ui.buttonBoxPatient.buttons()[1].clicked.connect(self.close)
        if mode != -1:
            self.ui.buttonBoxPatient.buttons()[0].clicked.connect(lambda: self.change_patient(mode))
            self.show_pat(mode)
        else:
            self.ui.buttonBoxPatient.buttons()[0].clicked.connect(self.add_patient)

    def show_pat(self, mode):
        self.ui.PatientEdit.setText(patient_list[mode].name)
        self.ui.DisEdit.setText(", ".join(patient_list[mode]._diseases))

    def read_patient(self, pat=None) -> Optional[Patient]:
        new_patient = Patient(self.ui.PatientEdit.displayText())
        # check that patient is already exist
        try:
            if new_patient.name == "":
                raise Exception("Поле ФИО не заполнено")
            for i in patient_list:

                if i.name == new_patient.name and pat != i:
                    raise Exception("Такой пациент уже существует")
            # end of check
            for j in re.findall(r"\w+", self.ui.DisEdit.displayText()):
                new_patient.add_disease(j)

        except Exception as e:
            msg = QtWidgets.QMessageBox()
            msg.setStyleSheet("QLabel{min-width: 75cpx;}")
            msg.setStyleSheet("QLabel{min-height: 70px;}")
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(e.args[0])
            msg.setWindowTitle("Ошибка")
            msg.exec()
            new_patient = None
        return new_patient

    def add_patient(self):
        pat = self.read_patient()
        if pat:
            patient_list.append(pat)
            self.close()

    def remove_patient(self):
        pass

    def change_patient(self, changedPat):
        d = self.read_patient(patient_list[changedPat])
        if d:
            patient_list[changedPat].change_data(d)
            self.close()


app = QtWidgets.QApplication([])
application = MyMainWindow()
application.show()
sys.exit(app.exec())
