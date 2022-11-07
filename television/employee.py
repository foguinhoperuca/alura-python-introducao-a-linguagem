class Hipster:
    def __str__(self):
        return f'Hipster, {self.name}'


class Employee:
    def __init__(self, name=None):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def show_tasks(self):
        return f"[EMPLOYEE] My tasks is... {self.__name}"

    def timeclock(self):
        return f"timeclock... {self.__name}"


class Caelum(Employee):
    def show_tasks(self):
        return f"[Caelum] show my (Caelumer) tasks... {self.name}"

    def find_monthly_course(self, month=None):
        return f"[CAELUM] the course of month is: {month} - {self.name}" if month else f'[CAELUM] Show all courses!!{self.name}'


class Alura(Employee):
    def show_tasks(self):
        return f"[ALURA] my tasks Alurete! {self.name}"

    def find_questions_without_answers(self):
        return f"[ALURA] show questions without answers in forum. {self.name}"


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


class Senior(Hipster, Alura, Caelum):
    pass


if __name__ == "__main__":
    print("Employee Caelum")

    jose = Junior(name="José")
    print(jose.find_questions_without_answers())
    print(jose.show_tasks())

    luan = Pleno(name="Luan")
    print(luan.find_questions_without_answers())
    print(luan.find_monthly_course())
    print(luan.show_tasks())

    jeff = Senior(name="Jeff")
    print(jeff)