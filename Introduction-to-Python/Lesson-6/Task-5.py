# 5. Реализовать класс Stationery (канцелярская принадлежность). определить в нём атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер); в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение; создать экземпляры классов и проверить, что выведет описанный метод для
# каждого экземпляра.

class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title
        print(f'Создан объект "{self.title}".')

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


my_brush = Stationery('кисть')
my_brush.draw()

my_pen = Pen('ручка')
my_pen.draw()

my_pencil = Pencil('карандаш')
my_pencil.draw()

my_handle = Handle('маркер')
my_handle.draw()
