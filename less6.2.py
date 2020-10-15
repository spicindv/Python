class Road:
    __length = ['длина']
    __width = ['ширина']

    def __init__(self, length, width) :
        self.length = length
        self.width = width
        print('Для 10 километров дороги необходимо')

    def intake(self):
        self.weigth = 25000
        self.thickness = 0.05
        intake = self.length * self.width * self.weigth * self.thickness / 1000
        print(f'{intake} тон Асфальта')

road_to_village = Road (10000, 20)
road_to_village.intake()