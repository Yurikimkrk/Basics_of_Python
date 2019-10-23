# 5.Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
new_f = input("Enter the name of file (without extension) - ")
try:
    with open(new_f + ".txt", "w") as f_w:
        f_w.write(input("Enter the numbers split by space - "))
    with open(new_f + ".txt") as f_r:
        print(f"Sum of numbers in the file {new_f+'.txt'} = {sum([int(i) for i in f_r.read().split()])}")
except IOError:
    print("Input/output error, maybe illegal character in file name (like / ? < and other)")
except ValueError:
    print("Input numbers!")
