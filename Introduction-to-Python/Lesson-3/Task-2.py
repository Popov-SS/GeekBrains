# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def info(name, last_name, birth_year, city, email, phone):
    print(f"Имя - {name}, Фамилия - {last_name}, Год рождения - {birth_year}, Город проживания - {city}, Адрес "
          f"электронной почты - {email}, Телефон - {phone}")


columns = ['имя', 'фамилию', 'год рождения', 'город проживания', 'email', 'телефон']
user_input = []
for i in columns:
    user_input.append(input(f"Введите {i}: "))
info(name=user_input[0], last_name=user_input[1], birth_year=user_input[2], city=user_input[3], email=user_input[4],
     phone=user_input[5])
