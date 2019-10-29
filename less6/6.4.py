# 4.Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево). А также несколько методов: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).

class Auto:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print("the car went")

    def stop(self):
        print("the car stop")

    def turn(self, direction):
        if direction == "right":
            print("the car turned right")
        if direction == "left":
            print("the car turned left")


class TownCar(Auto):
    is_police = False


class SportCar(Auto):
    is_police = False


class WorkCar(Auto):
    is_police = False


class PoliceCar(Auto):
    is_police = True


car_1 = TownCar(200, "blue", "Volvo")
print(f"{car_1.name}, color - {car_1.color}, max speed - {car_1.speed}km/h. Is that a police car? - {car_1.is_police}")
car_1.go()
car_1.turn("right")
car_1.turn("left")
car_1.stop()
car_2 = PoliceCar(240, "white", "Ford")
print(f"{car_2.name}, color - {car_2.color}, max speed - {car_2.speed}km/h. Is that a police car? - {car_2.is_police}")
car_1.go()
car_1.turn("left")
car_1.stop()