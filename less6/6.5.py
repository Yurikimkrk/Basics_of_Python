# 5.Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три
# дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = "draw"
    def draw(self):
        return "Start Draw."

class Pen(Stationery):
    def draw(self):
        return f"We continue to {self.title}. we trace the contours with a pen."

class Pencil(Stationery):
    def draw(self):
        return f"We continue to {self.title}. we draw the contours of the picture with a pencil."

class Handle(Stationery):
    def draw(self):
        return f"We continue to {self.title}. we paint the picture with a handle."

draw_pict = Stationery()
step_1 = Pencil()
step_2 = Pen()
step_3 = Handle()
print(f"{draw_pict.draw()}\n {step_1.draw()}\n {step_2.draw()}\n {step_3.draw()}")