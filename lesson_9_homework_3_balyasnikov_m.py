class Worker:
    def __init__(self, name, surname, position, **kwargs):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = kwargs


class Position(Worker):
    def __init__(self, name, surname, position, **kwargs):
        super().__init__(name, surname, position, **kwargs)

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


worker_1 = Position('Ivan', 'Ivanovich', '1C Programmer', wage=10000, bonus=7640)

worker_1.get_full_name()
worker_1.get_total_income()
