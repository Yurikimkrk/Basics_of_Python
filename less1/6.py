# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил
# a километров. Каждый день спортсмен увеличивал результат на 10% относительно
# предыдущего. Требуется определить номер дня, на который общий результат спортсмена
# составить не менее b километров. Программа должна принимать значения параметров
# a и b и  выводить одно натуральное число - номер дня.

a = input("Input positive integer (km first day): ")
b = input("Input positive integer (km check day): ")
while not a.isdigit() or not b.isdigit() or a == "0" or b == "0":
    print("Positive integers! Please, reEnter")
    a = input("Input positive integer (km first day): ")
    b = input("Input positive integer (km check day): ")
a = int(a)
b = int(b)
day = 1
while b > a:
    a = a * 1.1
    day += 1
print(f"On day {day} sportsman ran at least {b} km")
