# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
# строке.

file = open('file-2.txt', 'r', encoding='utf-8')
content = file.readlines()
# Разделяем элементы content на слова и записываем длину этих разделенных элементов
words_in_line = [len(i.split()) for i in content]
print(f'В файле {len(content)} строки, в каждой {words_in_line} слова.')
file.close()
