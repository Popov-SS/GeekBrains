# 1. Создать класс TrafficLight (светофор). определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный; в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный; продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение; переключение между режимами должно осуществляться только в указанном
# порядке (красный, жёлтый, зелёный); проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from time import sleep
from termcolor import cprint

class TrafficLight:
    __color = ''

    def __init__(self):
        print('The traffic light is created. Currently not showing any light.')

    def running(self, duration):
        self.__color = 'Red'
        cprint(f'The traffic light is operational. Currently showing {self.__color} light.', self.__color.lower())
        sleep(7)
        self.__color = 'Yellow'
        cprint(f'The traffic light has changed and is now showing {self.__color} light.', self.__color.lower())
        sleep(3)
        self.__color = 'Green'
        cprint(f'The traffic light has changed and is now showing {self.__color} light. Traffic has started.', self.__color.lower())
        sleep(duration)
        self.__color = 'Yellow'
        cprint(f'The traffic light has changed and is now showing {self.__color} light. Traffic is about to stop.', self.__color.lower())
        sleep(3)
        self.__color = 'Red'
        cprint(f'The traffic light has changed and is now showing {self.__color} light. Traffic has stopped.', self.__color.lower())


my_tlight = TrafficLight()
my_tlight.running(int(input('Введите длительность зелёного сигнала (в секундах): ')))