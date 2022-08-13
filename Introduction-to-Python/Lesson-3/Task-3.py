# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух
# аргументов.

def sum_largest(n_1, n_2, n_3):
    n_1, n_2, n_3 = map(int, [n_1, n_2, n_3])
    numbers = [n_1, n_2, n_3]
    return sum(numbers) - min(numbers)


a, b, c = map(int, input('Введите 3 числа: ').split())
print(sum_largest(a, b, c))
