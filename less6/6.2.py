# 2.Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного
# полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f"length - {self._length}, width - {self._width}")

    def asphalt(self, mass, thickness):
        print(f"Total mass of asphalt to cover all road = {self._length * self._width * mass * thickness} kg")


try:
    road_1 = Road(int(input("Enter the roads length (m) - ")), int(input("Enter the roads width (m) - ")))
    road_1.asphalt(int(input("Enter the asphalt mass for 1 sq.m. and 1 cm thickness (kg) - ")),
                   int(input("Enter the thickness of asphalt (cm) - ")))
except ValueError:
    print("Enter the numbers! Stop the program")
