# 7.Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, complex_number):
        self.complex_number = complex_number

    def __str__(self):
        return str(f"Complex number - {self.complex_number}")

    def __add__(self, other):
        return ComplexNumber(self.complex_number + other.complex_number)

    def __mul__(self, other):
        return ComplexNumber(self.complex_number * other.complex_number)


comp_num_1 = ComplexNumber(3 + 7j)
comp_num_2 = ComplexNumber(77 + 0j)
comp_num_3 = ComplexNumber(4.44 + 0.09j)

print(comp_num_1)
# Complex number - (3+7j)
print(comp_num_2*comp_num_3)
# Complex number - (341.88000000000005+6.93j)
print(comp_num_1+comp_num_3)
# Complex number - (7.44+7.09j)
# all calculations are correct!