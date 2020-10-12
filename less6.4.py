class Car:

    speed = None
    color = None
    name = None
    is_police = None

    def __init__(self, name, speed, color, is_police):
        self.color = color
        self.name = name
        self.speed = speed
        self.police = is_police

    @staticmethod
    def go():
        return 'Машина поехала!'
    @staticmethod
    def turn(direction):
        return 'машина поаорачивает!' + direction
    @property
    def stop(self):
        return 'Машина остоновилась!'
    def show_speed(self):
        return 'Скорость Машины!'

class TownCar(Car):
    def _init_ (self, name, speed , color ):
       super().__init__ (name, speed , color)

    def show_speed(self) :
         print(f'скорость TownCar {self.name} is {self.speed}')
         if self.speed > 40 :
            return f'Максимальная скорость {self.name} разрешенная для TownCar'
         else :
            return f'{self.name}'

class SportCar(Car):
    def __init__(self, name, speed, color ) :
        super().__init__( name, speed, color)

class WorkCar(Car):
    def __init__(self, speed, color, name) :
        super().__init__(speed, color, name)

    def show_speed(self) :
         print(f'скорость городского автомобиля {self.name} is {self.speed}')
         if self.speed > 60 :
            return f'Максимальная скорость {self.name} разрешенная для WorkCar'
         else :
            return f'{self.name}'

class PoliceCar(Car):
    def __init__(self, speed, color, name ):
        super().__init__(speed, color, name )

matiz = TownCar ('matiz', 40, 'black')
nissan = SportCar ('nissan', 180, 'red')
ford = WorkCar ('ford', 60, 'white')
skoda = PoliceCar ('skoda', 180, 'red')
print (f'matiz.TownCar', '40.speed', 'black.color')
print (matiz.go(), matiz.turn('City'), matiz.stop)
print (f'nissan.SportCar', '180.speed', 'red.color')
print (nissan.go(), nissan.turn('City'), nissan.stop)
print (f'ford.WorkCar', '60.speed', 'white.color')
print (ford.go(), ford.turn('City'), ford.stop)
print (f'skoda.PoliceCar', '180.speed', 'red.color')
print (skoda.go(), skoda.turn('City'), skoda.stop)




