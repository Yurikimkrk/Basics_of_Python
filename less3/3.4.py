# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
# функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции
# возведения числа в степень.


def my_func(x, y):
    # function takes numbers and returns 'x' in 'y' degree
    # verify that the numbers are entered correctly
    try:
        x, y = float(x), int(y)
        if x<=0 or y>=0:
            print("first number - positive, second - negative integer! Restart program\n")
        else:
            print(f"{x} in degree {y} = {x ** y}\n")
    except ValueError:
        print("Enter the numbers! Restart program\n")



while True:
    if input("'Q' to exit, Any key to continue program: ").upper() == "Q":
        break
    my_func(input("Enter any positive number: "), input("Enter any negative integer(degree): "))
