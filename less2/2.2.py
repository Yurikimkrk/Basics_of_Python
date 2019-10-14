# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить
# на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

list_len = input("Input list len: ")
while not list_len.isdigit() or list_len == "0":
    print("Positive integers!")
    list_len = input("Input list len: ")
new = []
for i in range(0, int(list_len)):
    new.append(input(f"Input element {i + 1}: "))
print(f"Users list:\n{new}")
x = 0
for j in range(0, int(list_len) // 2):
    new[x], new[x + 1] = new[x + 1], new[x]
    x += 2
print(f"Modified list:\n{new}")
