# 4. Реализуйте базовый класс Car. у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (
# куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля; для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Создана машина {self.name}')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        print(self.speed, 'Вы движетесь слишком быстро' if self.speed > 60 else '')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость: {self.speed} км/ч.', 'Вы движетесь слишком быстро.' if self.speed > 40 else '')


class PoliceCar(Car):
    pass


my_sportcar = SportCar(90, 'red', 'Ferrari', False)
my_sportcar.go()
my_sportcar.turn('направо')
my_sportcar.stop()

my_workcar = WorkCar(50, 'black', 'Toyota', False)
my_workcar.go()
my_workcar.show_speed()
my_workcar.stop()