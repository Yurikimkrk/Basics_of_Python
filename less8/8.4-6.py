# 4-6.Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники./Разработать
# методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь./Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на склад, нельзя
# использовать строковый тип данных.
warehouse = {}
equip_in_dep = {}


class Warehouse:
    @staticmethod
    def sent_to_dep(name, quantity, dep):
        if warehouse.get(name, 0) < quantity:
            print(f"We don't have {quantity} {name} to send now")
        else:
            warehouse[name] = warehouse.get(name, 0) - quantity
            if dep not in equip_in_dep.keys():
                equip_in_dep[dep] = [{name: quantity}]
            else:
                for i in range(len(equip_in_dep[dep])):
                    if name in equip_in_dep[dep][i].keys():
                        equip_in_dep[dep][i] = {name: (equip_in_dep[dep][i][name] + quantity)}
                        break
                else:
                    equip_in_dep[dep] = equip_in_dep[dep] + [{name: quantity}]


class OfficeEquipment:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def reception_equipment(self, quantity):
        warehouse[self.name] = warehouse.get(self.name, 0) + quantity


class Printer(OfficeEquipment):
    def __init__(self, name, color=False):
        super().__init__(name)
        self.color = color
        self.name = f"{name} printer"

    def __str__(self):
        return f"{self.name} it's color printer" if self.color else f"{self.name} it's black-white printer"


class Scanner(OfficeEquipment):
    def __init__(self, name, quality):
        super().__init__(name)
        self.quality = quality
        self.name = f"{name} scanner"

    def __str__(self):
        return f"{self.name} can scanned list with {self.quality} quality"


class Copier(OfficeEquipment):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed
        self.name = f"{name} copier"

    def __str__(self):
        return f"{self.name} can make {self.speed}"


xerox = Copier("xerox", "15copy/min")
print(xerox)  # xerox copier can make 15copy/min
toshiba = Copier("toshiba", "10copy/min")
print(toshiba)  # toshiba copier can make 10copy/min
brother = Printer("brother", True)
print(brother)  # brother printer it's color printer
canon = Scanner("canon", "high")
print(canon)  # canon scanner can scanned list with high quality
xerox.reception_equipment(7)
Warehouse.sent_to_dep("xerox copier", 8, "Main office")  # We don't have 8 xerox copier to send now
xerox.reception_equipment(3)
toshiba.reception_equipment(9)
canon.reception_equipment(12)
Warehouse.sent_to_dep("xerox copier", 2, "Main office")
Warehouse.sent_to_dep("xerox copier", 6, "Moscow department")
Warehouse.sent_to_dep("toshiba copier", 3, "Main office")
Warehouse.sent_to_dep("toshiba copier", 2, "Moscow department")
Warehouse.sent_to_dep("toshiba copier", 3, "Moscow department")
Warehouse.sent_to_dep("canon scanner", 4, "Main office")
Warehouse.sent_to_dep("canon scanner", 4, "Moscow department")
print(f"Warehouse - {warehouse}")
# Warehouse - {'xerox copier': 2, 'toshiba copier': 1, 'canon scanner': 4}
print(f"Equipment in departments - {equip_in_dep}")
# Equipment in departments -
# {'Main office': [{'xerox copier': 2}, {'toshiba copier': 3}, {'canon scanner': 4}],
# 'Moscow department': [{'xerox copier': 6}, {'toshiba copier': 5}, {'canon scanner': 4}]}
