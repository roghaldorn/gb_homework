class  Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Я ручка!')

class Pencil(Stationery):
    def draw(self):
        print('А я карандаш')

class Handle(Stationery):
    def draw(self):
        print('А я маркер')


obj_Base = Stationery('бумага')
obj_0 = Pen('шариковая ручка')
obj_1 = Pencil('цветной карандаш')
obj_2 = Handle('черный фломастер')

for obj in obj_Base, obj_0, obj_1, obj_2:
    obj.draw()