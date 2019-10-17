# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
# сумму наибольших двух аргументов.


def my_func(num1, num2, num3):
    # function takes numbers and returns the sum of the two largest numbers
    # verify that the numbers are entered correctly
    try:
        numbers = [float(num1), float(num2), float(num3)]
        print(f"Sum of the two largest numbers = {sum(numbers) - min(numbers)}")
    except ValueError:
        print("Enter the numbers! Restart program")


while True:
    if input("'Q' to exit, Any key to continue program: ").upper() == "Q":
        break
    my_func(input("Enter any number(1): "), input("Enter any number(2): "), input("Enter any number(3): "))