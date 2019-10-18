# 2.Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых
# больше предыдущего элемента. Подсказка: элементы, удовлетворяющие условию, оформить в виде
# списка. Для формирования списка использовать генератор.

import random as r

my_list = [r.randint(1, 100) for i in range(10)]
print(f"Main list - {my_list}")

new_list = []
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        new_list.append(my_list[i])

print(f"New list - {new_list}")
