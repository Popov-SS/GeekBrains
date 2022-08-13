# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться
# с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(a):
    a = str(a)
    if a.islower() and all(ord(c) in list(range(97, 123)) for c in a):
        return a.title()


user_input = input('Введите строку. Функция работает только со словами из маленьких латинских букв: ').split()
user_input = list(map(int_func, user_input))
result = ''
for i in user_input:
    result += str(i) + ' '
print(result)
