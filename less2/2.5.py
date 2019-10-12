# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных
# чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен
# разместиться после них. Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [95, 91, 91, 87, 84, 84, 84, 79, 72, 66, 44, 44, 12]
rating = input("Enter the new rating element: ")
while not rating.isdigit() or rating == "0":
    print("rating its positive integer")
    rating = input("Enter the new rating element: ")
rating = int(rating)
if rating in my_list:
    doubles = [index for index, v in enumerate(my_list) if v == rating]
    my_list.insert(doubles[-1] + 1, f"!{rating}!")
else:
    my_list.append(rating)
    my_list.sort(reverse=True)
print(my_list)

# my_list = [7, 5, 3, 3, 2]
# rating = input("Enter the new rating element: ")
# while not rating.isdigit() or rating == "0":
#     print("rating its positive integer")
#     rating = input("Enter the new rating element: ")
# rating = int(rating)
# my_list.append(rating)
# my_list.sort(reverse=True)
# print(my_list)
