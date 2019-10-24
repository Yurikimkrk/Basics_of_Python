# 7.Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки. Необходимо вычислить прибыль
# каждой компании и среднюю прибыль. Реализовать список, содержащий словарь (название фирмы
# и прибыль) и словарь с одним элементом (средняя прибыль). Добавить в первый словарь еще
# один элемент, содержащий результат вычисления отношения прибыли к убыткам. Итоговый список
# сохранить в файл.

# text in the file
# Yota Close_corp 100000 50000
# Megafon Public_corp 200000 130000
# BeeLine Close_corp 180000 100000
# MTC Public_corp 150000 60000

corp = [{}, {}]
try:
    with open(input("Enter the name of the file to open (without extension) - ") + ".txt") as f:
        my_list = [line.split() for line in f]
        total_profit = 0
        for i in range(len(my_list)):
            corp[0][my_list[i][0]] = (int(my_list[i][2]) - int(my_list[i][3]), int(my_list[i][2]) / int(my_list[i][3]))
            total_profit += int(my_list[i][2]) - int(my_list[i][3])
        corp[1]["Average profit"] = total_profit / len(my_list)
        print(corp)
    with open(input("Enter the name of new file (without extension) - ") + ".txt", "w") as new:
        print(*corp, file=new)
except IOError:
    print("Input/output error, maybe such a txt file doesn't exist")
