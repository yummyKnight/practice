from typing import cast, List, Dict, Optional, Type


class Person:
    def __init__(self, name: str):
        self.name = name


class Patient(Person):
    g_diseases: Dict[str, int] = dict()

    def __init__(self, name: str):  # tuple or list
        Person.__init__(self, name)
        self.__diseases: List[str] = list()

    def create_ref(self):
        pass

    def add_disease(self, disease: str):
        if disease in Patient.g_diseases.keys():
            Patient.g_diseases[disease] += 1
        else:
            Patient.g_diseases[disease] = 1
        self.__diseases.append(disease)

    def __del__(self):
        for i in self.__diseases:
            Patient.g_diseases[i] -= 1
            if Patient.g_diseases[i] <= 0:
                del Patient.g_diseases[i]


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
            return False
        else:
            return True

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
