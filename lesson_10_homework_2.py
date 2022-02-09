from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_cons(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__}'


class Coat(Clothes):
    def __init__(self, size=0):
        self.size = size
        self._fabric_cons = 0

    def __str__(self):
        return f'{super().__str__()} with size {self.size}'

    @property
    def fabric_cons(self):
        self._fabric_cons = self.size / 0.6 + 0.5
        return self._fabric_cons


class Suit(Clothes):
    def __init__(self, growth=0):
        self.growth = growth
        self._fabric_cons = 0

    def __str__(self):
        return f'{super().__str__()} with growth {self.growth}'

    @property
    def fabric_cons(self):
        self._fabric_cons = 2 * self.growth + 0.3
        return self._fabric_cons


suit_1 = Coat(24)
suit_2 = Suit(13)

print(suit_1)
print(suit_1.fabric_cons)
print(suit_2)
print(suit_2.fabric_cons)
