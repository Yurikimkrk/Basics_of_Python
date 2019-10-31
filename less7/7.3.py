# 3. Реализовать программу работы с клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны выполнять увеличение,
# уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе
# деления должно осуществляться округление значения до целого числа.
# В классе необходимо реализовать метод make_cell(), принимающий экземпляр класса и количество
# клеток в ряду. Метод должен возвращать строку виду *****\n*****\n*****..., где количество клеток
# между \n равно переданному аргументу, а количество рядов определяется, исходя из общего количества
# клеток.
# При создании экземпляра клетки должна происходить перезапись параметра, который хранит количество
# клеток. Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(f"Number of cells - {self.number}")

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(int((self.number / other.number) // 1))

    def make_cell(self, cell_in_row):
        x = ""
        for i in range(int((self.number / cell_in_row // 1))):
            x += f'{"*" * cell_in_row}\\n'
        x += f'{"*" * (self.number % cell_in_row)}'
        return x


first_c = Cell(24)
print(first_c)
# Number of cells - 24
second_c = Cell(10)
print(first_c / second_c)
# Number of cells - 2
print(first_c.make_cell(7))
# *******\n*******\n*******\n***