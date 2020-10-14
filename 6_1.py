class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        from time import sleep
        from itertools import cycle
        color = ['красный', 'желтый', 'зеленый']
        for i in cycle(color):
            time.sleep(7)

            if input('') == '':
                break
            print(i)
tr = TrafficLight()
tr.running()
