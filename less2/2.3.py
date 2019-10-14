# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# # относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
seasons = {
    1: "winter",
    2: "winter",
    3: "spring",
    4: "spring",
    5: "spring",
    6: "summer",
    7: "summer",
    8: "summer",
    9: "autumn",
    10: "autumn",
    11: "autumn",
    12: "winter",
}
months = ["january", "february", "march", "april", "may", "june",
          "july", "august", "september", "october", "november", "december"]
users_m = input("Input number of month (1 - 12): ")
while not users_m.isdigit() or int(users_m) > 12 or int(users_m) < 1:
    print("12 months!")
    users_m = input("Input number of month: ")
print(f"{months[int(users_m) - 1]} is {seasons[int(users_m)]}")
