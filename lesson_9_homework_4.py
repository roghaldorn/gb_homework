class Car:
    def __init__(self, speed, color, is_police):
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Car is going.')

    def stop(self):
        print('Car is stopped.')

    def turn(self, direction):
        print(f'Car turn {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости: {self.speed}')
        else:
            print(self.speed)



class SportCar(Car):
    def __init__(self, speed, color, model):
        super().__init__(speed, color)
        self.model = model


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости: {self.speed}')
        else:
            print(self.speed)


class PoliceCar(Car):
    pass


car_1 = WorkCar(78, 'yellow', True)
car_1.show_speed()
car_1.go()