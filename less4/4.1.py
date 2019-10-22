# 1.Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы
# сотрудника.В расчете необходимо использовать формулу: (выработка в часах*ставка в час)+премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, working_hours, hours_rate, prize = argv


# parameters - 160 10 550
def salary(working_hours, hours_rate, prize):
    return int(working_hours) * int(hours_rate) + int(prize)


print(f"Salary per month - {salary(working_hours, hours_rate, prize)} $")
