# 3.Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на
# словарь, содержащий элементы: оклад и премия, например, {"profit": profit, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_full_profit).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
salary = {"director_profit": 100000, "director_bonus": 50000,
          "accountant_profit": 80000, "accountant_bonus": 40000,
          "worker_profit": 40000, "worker_bonus": 30000,
          "manager_profit": 50000, "manager_bonus": 35000}


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def get_full_name(self):
        print(f"{self.position} - {self.name + ' ' + self.surname}")

    def get_full_profit(self):
        print(
            f"{self.position}s full profit - {salary[self.position + '_profit'] + salary[self.position + '_bonus']} $")


worker_1 = Position("Yuri", "Kim", "director")
worker_1.get_full_name()
worker_1.get_full_profit()
worker_2 = Position("Ivan", "Ivanov", "manager")
worker_2.get_full_name()
worker_2.get_full_profit()
