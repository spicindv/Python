class Worker:

    def __init__(self, name, surname, position, profit, bonus) :
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus) :
        super().__init__(name, surname, position, profit, bonus)
        self.__income = {'profit' : self.profit, 'bonus' : self.bonus}

    def get_full_name(self) :
        return self.name + ' ' + self.surname

    @property

    def get_full_profit(self):
        return self.__income

a = Position('Peter', 'The Great', 'a', 10000, 2500)
print(a.get_full_name(), a.get_full_profit)