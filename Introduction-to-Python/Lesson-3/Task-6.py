# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(a):
    a = str(a)
    if a.islower() and all(ord(c) in list(range(97, 123)) for c in a):
        return a.title()


user_str = input('Введите слово. Функция работает только со словами из маленьких латинских букв: ')
print(int_func(user_str))
