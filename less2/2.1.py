# 1.Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

new = [15, -24, "great", 5.5, True, [1, 2, 3], {"name": "Yuri", "surname": "Kim"}]
for i in new:
    print(f"{i} - {type(i)}")
