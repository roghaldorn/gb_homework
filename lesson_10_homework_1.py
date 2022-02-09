class Matrix:
    def matrix_checker(callback):
        def wrapper(*args):
            for element in args:
                if not isinstance(element, Matrix):
                    raise ValueError('Use Matrix, not integer!')
            return callback(*args)

        return wrapper

    def __init__(self, *args):
        self.matrix = args[0]
        self.length = len(args[0][0])
        self.heigth = len(args[0])

    def __str__(self):
        self._str_matrix = ''
        for length in self.matrix:
            for element in length:
                self._str_matrix += str(element)
                self._str_matrix += ' '
            self._str_matrix += '\n'
        return self._str_matrix

    @matrix_checker
    def __add__(self, other):
        new_matrix = [[self.matrix[length][heigth] + other.matrix[length][heigth] for heigth in range(self.heigth)] for
                      length in range(self.length)]
        return Matrix(new_matrix)


matrix_1 = Matrix([[1, 2, 3], [3, 2, 1], [6, 5, 4]])
matrix_2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

print(matrix_1 + matrix_2)
