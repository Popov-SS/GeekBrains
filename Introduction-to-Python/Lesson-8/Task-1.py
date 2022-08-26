# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.
#
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):
        if cls.check_date(date):
            return list(map(int, (str(date).split('-'))))
        else:
            return 'Дата записана неверно'

    @staticmethod
    def check_date(date):
        date = str(date).split('-')
        if int(date[0]) in list(range(1, 32)) and int(date[1]) in list(range(1, 13)):
            return True


my_date = Date(input('Введите дату в формате "день-месяц-год": '))
print(my_date.get_date(my_date.date))
