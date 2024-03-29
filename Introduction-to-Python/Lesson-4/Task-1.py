# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте
# в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv

_, work_time, labor_cost, bonus = argv
salary = int(work_time) * int(labor_cost) + int(bonus)

print(f"За {work_time} часов работы при ставке {labor_cost} в час и премии {bonus} работник получит {salary}")
