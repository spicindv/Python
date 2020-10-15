class Worker:
    def __init__(self, name, surname, position, income):
        self.my_name = name
        self.my_surname = surname
        self.my_position = position
        self._my_income = income

class Position(Worker):
    def get_full_name(self):
        print(self.my_name, self.my_surname, self.my_position)
    def get_total_income(self):
        print(self._my_income)

psn = Position('Den', 'Spicin', 'Starter')
psn.get_full_name()
psn.get_total_income()
