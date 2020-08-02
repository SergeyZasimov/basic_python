class Cell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num > other.num:
            return self.num - other.num
        else: return 'Отрицательное количество клеток'

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        try:
            return round(self.num / other.num)
        except ZeroDivisionError:
            return 'Деление на ноль'

    def make_order(self, value):
        order =  '\\n'.join(['*' * value for i in range(self.num // value)])
        if self.num % value != 0:
            order = order + ('\\n' + '*' * (self.num % value))
        return order

if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(4)
    cell_3 = Cell(12)
    print('Сложение', cell_1 + cell_2)
    print('Вычитание', cell_1 - cell_2)
    print(cell_2 - cell_3)
    print('Умножение', cell_1 * cell_2)
    print('Деление', cell_1 / cell_2)
    print(cell_1.make_order(5))
    print(cell_3.make_order(5))
