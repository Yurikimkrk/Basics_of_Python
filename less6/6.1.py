# 1.Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый. Время перехода между режимами должно составлять
# 7 и 2 секунды. Проверить работу примера, создав экземпляр и вызвав описанный метод.

class TrafficLight:
    __color = "red"

    def running(self, time1, time2):
        print(f"{trl._TrafficLight__color} light")
        time_count = time1
        for i in range(time_count, 0, -1):
            print(f'{i} seconds to switch')
        trl._TrafficLight__color = "yellow"
        print(f"{trl._TrafficLight__color} light")
        time_count = time2
        for i in range(time_count, 0, -1):
            print(f'{i} seconds to switch')
        trl._TrafficLight__color = "green"
        print(f"{trl._TrafficLight__color} light")


trl = TrafficLight()

trl.running(7, 2)
