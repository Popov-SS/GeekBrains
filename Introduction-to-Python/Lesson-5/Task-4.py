# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

file = open('file-4.txt', 'r', encoding='utf-8')
file_translated = open('file-4-translated.txt', 'w', encoding='utf-8')
content = ' '
translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
while content:
    content = file.readline()
    for i in translator:
        if i in content.split():
            content = content.replace(f'{i}', f'{translator[i]}')
    file_translated.write(content)
file.close()
file_translated.close()
