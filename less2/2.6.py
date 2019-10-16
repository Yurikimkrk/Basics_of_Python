# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
# единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные
# у пользователя. Пример готовой структуры:
# [   (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”}) ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {    “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]     }

goods = []
features = {"Name": "", "Price, rub": "", "Number": "", "Measure unit": ""}
analytics = {"Name": [], "Price, rub": [], "Number": [], "Measure unit": []}
count = 0
while True:
    if input("'Q' to exit, Any key to continue: ").upper() == "Q":
        break
    print(goods)
    count += 1
    for i in features.keys():
        x = input(f"Enter the {count} {i}: ")
        features[i] = int(x) if i == "Price, rub" or i == "Number" else x
        if features[i] not in analytics[i]:
            analytics[i].append(features[i])
    goods.append((count, features))
    print(f"\n Analytics: \n {'*' * 30}")
    for key, value in analytics.items():
        print(f'{key[:25]:>15}: {value}')
    print('*' * 30)
#
# goods = []
# numb = input("Enter the number of goods: ")
# while not numb.isdigit() or numb == "0":
#     numb = input("Error, enter the number of goods: ")
# for i in range(1, int(numb) + 1):
#     goods.append((i, {"Name": input(f"Enter the name of the {i} item: "),
#                       "Price, rub": int(input(f"Enter the price of the {i} item: ")),
#                       "Number": int(input(f"Enter the number of the {i} items: ")),
#                       "Measure unit": input(f"Enter the measure unit of the {i} item: ")}))
# print("-----------------------------List of products-----------------------------")
# for i in goods:
#     print(i)
# print("---------------------------------Analytics--------------------------------")
#
# name = []
# price = []
# number = []
# measure_unit = []
# for i in range(0, int(numb)):
#     if goods[i][1]["Name"] not in name:
#         name.append(goods[i][1]["Name"])
# for i in range(0, int(numb)):
#     if goods[i][1]["Price, rub"] not in price:
#         price.append(goods[i][1]["Price, rub"])
# for i in range(0, int(numb)):
#     if goods[i][1]["Number"] not in number:
#         number.append(goods[i][1]["Number"])
# for i in range(0, int(numb)):
#     if goods[i][1]["Measure unit"] not in measure_unit:
#         measure_unit.append(goods[i][1]["Measure unit"])
# analytics = {"Name": name, "Price, rub": price, "Number": number, "Measure unit": measure_unit}
# for key, values in analytics.items():
#     print(f'Unique "{key}" - {values}')
