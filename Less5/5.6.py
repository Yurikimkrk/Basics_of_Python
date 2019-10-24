# 6.Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# text in the file
# Physics: lecture - 3 practice - 1 lab - 2
# Mathematics: lecture - 2 practice - 3 lab - 1
# Physical culture: practice - 5

my_less = {}
try:
    with open(input("Enter the name of the file to open (without extension) - ") + ".txt") as f:
        my_list = [line.split(": ") for line in f]
        for i in range(len(my_list)):
            my_less[my_list[i][0]] = sum([int(y) for y in [x for x in my_list[i][1].split() if x.isdigit()]])
        print(my_less)
except IOError:
    print("Input/output error, maybe such a txt file doesn't exist")
