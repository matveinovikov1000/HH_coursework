class WorkVacancies:
    """Класс для работы с вакансиями"""

    def __init__(
        self, name=None, town=None, requirements=None, payment_from=0, payment_to=0
    ):
        self.name = name
        self.town = town
        self.requirements = requirements
        if payment_from == 0 and payment_to == 0:
            self.payment_from = 0
            self.payment_to = 0
            self.salary = 0
        elif payment_from != 0 and payment_to == 0:
            self.payment_from = payment_from
            self.payment_to = 0
            self.salary = self.payment_from
        elif payment_from == 0 and payment_to != 0:
            self.payment_from = 0
            self.payment_to = payment_to
            self.salary = self.payment_to
        elif payment_from != 0 and payment_to != 0:
            self.payment_from = payment_from
            self.payment_to = payment_to
            self.salary = (self.payment_from + self.payment_to) / 2

    def __le__(self, other):
        """Метод для сравнения зарплат вакансий"""
        return self.salary <= other.salary

    def __ge__(self, other):
        """Метод для сравнения зарплат вакансий"""
        return self.salary >= other.salary


if __name__ == "__main__":
    wv = WorkVacancies("Кузнец", "Челябинск", "Огнеупорность", 100, 150)
    wv1 = WorkVacancies("Дальнобойщик", "Воркута", "Категория Е", 200, 250)
    print(wv.name)
    print(wv.town)
    print(wv.requirements)
    print(wv.payment_from)
    print(wv.payment_to)
    print(wv.salary)
    print(type(wv.salary))
    print(wv >= wv1)
    print(wv <= wv1)
