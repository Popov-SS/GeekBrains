# 1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и
# строки и сохраните в переменные, затем выведите на экран.


# Эта программа работает как список покупок. Она может добавлять и убирать продукты, которые вводит пользователь.
pw = "Password"
shopping_list = ['Молоко', 'Сосиски', 'Хлеб', 'Сыр']

input_pw = input("Введите пароль: ")
if input_pw == pw:
    print("Добро пожаловать в Ваш список покупок.")
    while True:
        print("Сейчас в списке находятся: ", shopping_list)
        i = input('Хотите добавить или убрать предмет из списка? ')
        if i == 'добавить':
            i = input('Что нужно купить? ')
            shopping_list.append(i)
        elif i == 'убрать':
            i = input('Что нужно убрать? ')
            shopping_list.remove(i)
        elif i == 'закончить':
            break
        else:
            print('Нераспознанная команда. Пожалуйста, введите "добавить", "убрать" или "закончить".')
else:
    print('Неверный пароль.')
