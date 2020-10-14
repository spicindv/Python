class Road:
    def __init__(self, length, width):
        self._my_len = length
        self._my_width = width

    def roadmass(self):
        print(self._my_len * self._my_width * 25 * 5 / 1000)

my_r = Road(20, 5000)
my_r.roadmass()
