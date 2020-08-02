# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно. 
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class AbstractClothes(ABC):
    @abstractmethod
    def __init__(self, param):
        """
        Инициализация класса с соответствующим ему параметром
        """

    @abstractmethod
    def outlay(self):
        """
        Определение расхода ткани
        """

class Coat(AbstractClothes):
    """
    Пальто
    """
    def __init__(self, param):
        self.size = param

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value < 42:
            self.__size = 42
        elif value > 60:
            self.__size = 60
        else:
            self.__size = value

    def outlay(self):
        return round(self.size / 6.5 + 0.5)

class Suit(AbstractClothes):
    """
    Костюм
    """
    def __init__(self, param):
        self.height = param

    def height(self):
        return self.__height

    def set_height(self, value):
        self.__height = value / 100

    height = property(height, set_height)

    def outlay(self):
        return (2 * self.height + 0.3)


if __name__ == '__main__':
    coat1 = Coat(42)
    print('Пальто_1 =>', coat1.outlay())
    print()
    coat2 = Coat(39)
    print('Пальто_2 =>', coat2.outlay())
    print()
    suit = Suit(180)
    print('Костюм =>', suit.outlay())
    print()
    print(f'Общий объём => {coat1.outlay() + coat2.outlay() + suit.outlay()}')
