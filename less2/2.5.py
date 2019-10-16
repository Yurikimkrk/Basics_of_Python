# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных
# чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен
# разместиться после них. Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [95, 91, 91, 87, 84, 84, 84, 79, 72, 66, 44, 44, 12]

while True:
    print(f"Curent rating: {my_list}")
    rating = input("Enter the new rating element or Q to finish: ")
    if rating == "Q":
        print("End of program")
        break
    while not rating.isdigit() or rating == "0":
        print("rating its positive integer")
        rating = input("Enter the new rating element: ")
    rating = int(rating)
    if my_list.count(rating):
        my_list.insert(my_list.index(rating) + my_list.count(rating), rating)
    else:
        for n, i in enumerate(my_list):
            if rating > i:
                my_list.insert(n, rating)
                break
        else:
            my_list.append(rating)
