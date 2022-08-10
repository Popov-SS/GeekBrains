# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_n = int(input('Введите число '))
number = user_n
max_digit = 0
while number:
    if number % 10 > max_digit:
        max_digit = number % 10
    number //= 10

print(f'Самая большая цифра в числе {user_n} это {max_digit}')
