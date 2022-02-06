class Road:
    ASPHALT_ON_METER = 25.7  # по данным гугла
    ASPHALT_THICKNESS = 1

    def int_checker(callback):
        def wrapper(*args):
            for value in args:
                if isinstance(value, str):
                    raise ValueError('Please enter a integer!')
            return callback(*args)

        return wrapper

    @int_checker
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @int_checker
    def asphalt_mass(self, *args):
        if len(args) == 0:
            self.asphalt_on_meter = Road.ASPHALT_ON_METER
            self.asphalt_thinkess = Road.ASPHALT_THICKNESS
            print('Аргументы взяты по умолчанию.')
        else:
            self.asphalt_on_meter = args[0]
            self.asphalt_thinkess = args[1]
        self.mass = self._length * self._width * self.asphalt_on_meter * self.asphalt_thinkess / 1000

        print(
            f'{self._length} м*{self._width} м*{self.asphalt_on_meter} кг*{self.asphalt_thinkess} см = {self.mass} т.')


road_1 = Road(20, 5000)
road_1.asphalt_mass(25, 5)
