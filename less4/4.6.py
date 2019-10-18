# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

import itertools as it
# integers iterator with checking for integer
try:
    integers = iter(i for i in it.count(int(input("Enter starting integer: "))))
    print(f"first numbers in the 'integers' iterator: {next(integers)} {next(integers)} {next(integers)}\n")
except:
    print("Error, only integers!")
# cycle iterator
my_list = ['go', 1, 2, "hello"]
print(f"List - {my_list}")
cycle_iter = iter(i for i in it.cycle(my_list))
print(f"first elements in the 'cycle' iterator: {next(cycle_iter)} {next(cycle_iter)} "
      f"{next(cycle_iter)} {next(cycle_iter)} {next(cycle_iter)} {next(cycle_iter)}\n")
