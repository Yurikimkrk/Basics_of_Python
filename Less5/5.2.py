# 2.Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

try:
    with open(input("Enter the name of the file to open (without extension) - ") + ".txt") as f:
        my_list = [line.split() for line in f]
        print(f"Lines in current file - {len(my_list)}")
        for i in range(len(my_list)):
            print(f"Words in line {i+1} --> {len(my_list[i])}")
except IOError:
    print("Input/output error, maybe such a txt file doesn't exist")
