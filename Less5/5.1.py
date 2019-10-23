# 1.Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.

try:
    with open(input("Enter the name of file (without extension) - ") + ".txt", "w") as f:
        x, count = 1, 1
        while x != "":
            # fill the lines with the line number
            x = input(f"Enter the line № {count} (empty line to the end input)  - ")
            print(x, file=f)
            count += 1
        print(f"\nNew txt file successfully added and filled.\nEnd of program")
except IOError:
    print("Input/output error, maybe illegal character in file name (like / ? < and other)")
