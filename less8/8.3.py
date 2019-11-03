# 3.Создайте собственный класс-исключение, который должен проверять содержимое списка на отсутствие
# элементов типа строка и булево. Проверить работу исключения на реальном примере. Необходимо
# запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать
# типы данных элементов списка.
user_list = [5, "grand", -1.1, False, ["god", "dog"], {"key": "value"}, "run", 999, True]
# list for example. we can open some file with list (lecture 5)
filtered_list = []


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

for i in user_list:
    try:
        if isinstance(i, str):
            raise OwnError(f"'{i}' it's string type")
        elif isinstance(i, bool):
            raise OwnError(f"{i} it's bool type")
        else:
            filtered_list.append(i)
    except OwnError as err:
        print(err)
print(f'Filtered list - {filtered_list}')
