# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
# несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} GO!!!')

    def stop(self):
        print(f'{self.name} Stop.')

    def turn(self, direction):
        print(f'{self.name} повернула на{direction}.')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print('Превышение скорости!!!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print('Превышение скорости!!!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

townCar = TownCar(100, "white", "toyota")
sportCar = SportCar(200, "red", "Ferrari")
workCar = WorkCar(50, 'brown', "MAN")
policeCar = PoliceCar(150, 'blue', "Ford")

print(townCar.__class__)
for attr in list(townCar.__dict__):
    print(f'{attr} = {getattr(townCar, attr)}')

townCar.show_speed()
print()
print(sportCar.__class__)
sportCar.go()
sportCar.stop()
sportCar.turn("право")
print()
print(workCar.__class__)
workCar.show_speed()
print()
print(policeCar.__class__)
for attr in list(policeCar.__dict__):
    print(f'{attr} = {getattr(policeCar, attr)}')