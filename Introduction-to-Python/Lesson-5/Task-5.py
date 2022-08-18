# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import randint

file = open('file-5.txt', 'w+', encoding='utf-8')
for i in range(11):
    print(randint(1,100), file=file, end=' ')
file.seek(0)
content = file.readline().split()
print(f'Сумма чисел в файле: {sum(list(map(int, content)))}')
file.close()
