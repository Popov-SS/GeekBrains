# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

user_n = input('Введите число ')
n = int(user_n)
nn = int(user_n * 2)
nnn = int(user_n * 3)
result = n + nn + nnn
print(f'Вы ввели {user_n}. {n} + {nn} + {nnn} = {result}')
