# 1.Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
# @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
from datetime import date


class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f"Date without validation {self.date}"

    @classmethod
    def show_me_the_date(cls, date):
        day, month, year = list(map(int, date.split("-")))
        if Date.number_validation(day, month, year):
            return f"Date: {day}.{month}.{year}"
        else:
            return "Unknown date"

    @staticmethod
    def number_validation(day, month, year):
        try:
            date(year, month, day)
            return True
        except ValueError:
            return False


print(Date.show_me_the_date("5-13-2019"))
# Unknown date
print(Date.show_me_the_date("5-11-2019"))
# Date: 5.11.2019
print(Date("99-99-9999"))
# Date without validation 99-99-9999
