from typing import cast, List, Dict, Optional, Type
from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def change_data(self, Person):
        pass


class Patient(Person):
    g_diseases: Dict[str, int] = dict()

    def __init__(self, name: str):  # tuple or list
        Person.__init__(self, name)
        self._diseases: List[str] = list()

    def add_disease(self, disease: str):
        if disease in Patient.g_diseases.keys():
            Patient.g_diseases[disease] += 1
        else:
            Patient.g_diseases[disease] = 1
        self._diseases.append(disease)

    def add_diseases(self, diseases: List[str]):
        for i in diseases:
            self.add_disease(i)

    def change_data(self, another_patient):
        if self.name != another_patient.name:
            self.name = another_patient.name
        if self._diseases != another_patient._diseases:
            # del diseases
            self.del_diseases()
            self.add_diseases(another_patient._diseases)

    def __del__(self):
        self.del_diseases()

    def del_diseases(self):
        for i in self._diseases:
            Patient.g_diseases[i] -= 1
            if Patient.g_diseases[i] <= 0:
                del Patient.g_diseases[i]
        self._diseases = list()


class Period:
    def __init__(self, borL: float, borR: float):
        self.borL = borL
        self.borR = borR
        # ! validation

    def change_borders(self, newborL: float, newborR: float):
        self.borL = newborL
        self.borR = newborR

    def is_collision(self, another_period) -> bool:
        cast(Period, another_period)
        if self.borL <= another_period.borL <= self.borR or self.borL <= another_period.borR <= self.borR or \
                another_period.borL >= self.borL and another_period.borR <= self.borR:
            return True
        else:
            return False

    def __str__(self):
        return "{0:.2f} - {1:.2f}".format(self.borL, self.borR)


class Schedule:
    # week = ("Mon", "Tue", "Wed", "Thu", "Fri", "San", "Sat")
    week = ("ПН", "ВТ", "СР", "ЧТ", "ПТ")


class Doctor(Person):
    def __init__(self, spec: str, name: str, cabinet: int):
        super().__init__(name)
        self.spec = spec
        self.cabinet = cabinet
        self.timetable: Dict[str, Optional[Period]] = dict()
        for i in Schedule.week:
            self.timetable[i] = None

    def add_work(self, day_of_week: str, period: Period):  # one Doctor - one cabinet per day
        self.timetable[day_of_week] = period  # rewriting prev period

    def switch_cab(self, new_cabinet: int, old_cabinet, day_of_week: str):
        self.timetable[day_of_week][new_cabinet] = self.timetable[day_of_week].pop(old_cabinet)

    def change_data(self, another_doc):
        if self.spec != another_doc.spec:
            self.spec = another_doc.spec
        if self.name != another_doc.name:
            self.name = another_doc.name
        if self.cabinet != another_doc.cabinet:
            self.cabinet = another_doc.cabinet
        for i in self.timetable.keys():
            if self.timetable[i] != another_doc.timetable[i]:
                self.timetable[i] = another_doc.timetable[i]

    def del_work(self, day_of_week: str):
        if day_of_week in Schedule.week:
            self.timetable[day_of_week] = None
