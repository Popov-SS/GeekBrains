# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов
# списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
from random import randint

my_list = [randint(100, 1000) for i in range(5)]
print(my_list, reduce(lambda x, y: x * y, my_list))
