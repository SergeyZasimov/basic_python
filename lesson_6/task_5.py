# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки - {self.title}')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        Stationery.draw(self)
        print(f'{self.title.capitalize()} пишет письмо.')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        Stationery.draw(self)
        print(f'{self.title.capitalize()} рисует картину.')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        Stationery.draw(self)
        print(f'{self.title.capitalize()} чертит линию.')

pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")

for klass in [pen, pencil, handle]:
    klass.draw()
    print()