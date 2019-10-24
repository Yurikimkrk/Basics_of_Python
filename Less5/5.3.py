# 3.Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
# их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
# сотрудников. Выполнить подсчет средней величины дохода сотрудников.

try:
    with open(input("Enter the name of the file to open (without extension) - ") + ".txt") as f:
        # create a dict (worker: salary)
        workers = dict(line.split() for line in f)
        print(f"Salary less 20k have {', '.join([k for k in workers if int(workers[k]) < 20000])}")
        salaries = list(map(int, workers.values()))
        print(f"Average salary {(sum(salaries) / len(salaries)):.0f}")
except IOError:
    print("Input/output error, maybe such a txt file doesn't exist")
