# 4.Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

numerals = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
try:
    with open(input("Enter the name of the file to open (without extension) - ") + ".txt") as f:
        my_list = [line.split() for line in f]
        for i in my_list:
            # replace english numerals by russian
            i[0] = numerals[i[0]]
        with open(input("Enter the name of the new file(without extension) - ") + ".txt", 'w') as new:
            for i in range(len(my_list)):
                new.write(f'{" ".join(my_list[i])}\n')
except IOError:
    print("Input/output error, maybe such a txt file doesn't exist")
