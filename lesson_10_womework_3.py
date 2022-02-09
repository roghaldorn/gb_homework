class Cell:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f'{self.size}'

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        return Cell(self.size - other.size) if self.size - other.size > 0 else ValueError('Cell size is less than Zero')

    def __mul__(self, other):
        return Cell(self.size * other.size)

    def __floordiv__(self, other):
        return Cell(self.size // other.size)

    def __truediv__(self, other):
        return Cell(self.size // other.size)

    def make_order(self, line_size):  # самая сложная функция за весь курс (
        _final = ''
        for cell in range(1, self.size + 1):
            _final += '*'
            if cell % line_size == 0:
                _final += '\n'
        return _final


cell_1, cell_2 = Cell(12), Cell(3)

print(cell_1.make_order(5))
