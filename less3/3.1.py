# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def first_func(dividend, divider):
    # function takes dividend, divider and show the result of dividing
    # verify that the dividend and divider are entered correctly
    try:
        dividend, divider = float(dividend), float(divider)
        print(f"{dividend} / {divider} = {dividend / divider:.2f}")
    except ValueError:
        print("Enter the numbers!")
    except ZeroDivisionError:
        print("You can't divide by zero!")


while True:
    if input("'Q' to exit, Any key to continue program: ").upper() == "Q":
        break
    first_func(input("Enter the dividend: "), input("Enter the divider: "))
