# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата

import re


class Complex:
    def __init__(self, digit):
        if digit[0] != '-':
            digit = '+' + digit
        digit = re.findall(r'[0-9\.]+|[^0-9\.]+', digit)
        self.real = int(digit[0] + digit[1])
        self.im = int(digit[2] + digit[3])

    def __str__(self):
        return f'{self.real}{self.im:+}i'

    def __add__(self, other):
        return Complex(f'{self.real + other.real}{self.im + other.im:+}i')

    def __mul__(self, other):
        return Complex(f'{self.real * other.real - self.im * other.im}{self.real * other.im + self.im * other.real:+}i')


my_cn1 = Complex('5+3i')
my_cn2 = Complex('3-7i')
print(my_cn1 + my_cn2)
print(my_cn1 * my_cn2)
