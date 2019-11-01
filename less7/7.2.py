# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
# (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом
# проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
# и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу
# декоратора @property.


class Clothes:
    def __init__(self, name):
        self.name = name


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_exp(self):
        return 2 * self.height + 0.3


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_exp(self):
        return self.size / 6.5 + 0.5


armani = Suit("Armani", 1.82)
print(f"Fabric expenditure for suit - {armani.fabric_exp} m")
# Fabric expenditure for suit - 3.94 m
burberry = Coat("Burberry", 52)
print(f"Fabric expenditure for coat - {burberry.fabric_exp} m")
# Fabric expenditure for coat - 8.5 m