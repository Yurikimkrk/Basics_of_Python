# 2.Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его
# работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input("Enter dividend: ")
divider = input("Enter divider: ")
try:
    dividend = int(dividend)
    divider = int(divider)
    if divider == 0:
        raise OwnError("Divider can't be zero")
except ValueError:
    print("Input numbers")
except OwnError as err:
    print(err)
else:
    print(f"Result {dividend} / {divider} = {dividend / divider}")
