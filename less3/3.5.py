# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных
# пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже
# подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_func():
    # function takes numbers lines (split by space) and sum all elements
    # verify that the numbers are entered correctly
    while True:
        try:
            inp = input("Enter your numbers with a space('q' in any position to exit after sum):\n")
            num_line = inp.split()
            # check the "q" button for exit the program
            if "q" in num_line:
                try:
                    global summ
                    num_line = list(map(float, num_line[:num_line.index("q")]))
                    summ += sum(num_line)
                    print(f"Total sum = {summ}   End of program")
                    break
                except ValueError:
                    print("Enter the numbers!\n")
            num_line = list(map(float, num_line))
            summ += sum(num_line)
            print(f"Total sum = {summ}\n")
        except ValueError:
            print("Enter the numbers!\n")


summ = 0
my_func()
