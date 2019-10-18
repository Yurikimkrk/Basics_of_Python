# 4.Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать
# итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования
# в исходном списке. Для выполнения задания обязательно использовать генератор.

import random as r

my_list = [r.randint(1, 20) for i in range(20)]
print(f"Main list - {my_list}")

new_list = []
for i in range(len(my_list)):
    for j in range(len(my_list)):
        if my_list[i] == my_list[j] and i != j:
            break
    else:
        new_list.append(my_list[i])

print(f"New list - {new_list}")
