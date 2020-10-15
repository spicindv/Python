class Cloth:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return round(self.width / 6.5 + 0.5)

    def get_square_j(self):
        return round(self.height * 2 + 0.3)

    @property
    def get_sq_full(self):
        return str(f'Общий размер ткани \n'
                 f'{round(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')
class Coat(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(width / 6.5 + 0.5)

    def __str__(self):
        return f'Необходимое количество ткани для пальто {self.square_c}'

class Jacket(Cloth):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Необходимое количество ткани  для пиджака {self.square_j}'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
