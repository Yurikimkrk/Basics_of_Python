# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру
# в числе. Для решения используйте цикл while и арифметические операции.

n = int(input("enter a positive integer: "))
max_num = 0
while n > 0:
    last_num = n % 10
    if last_num > max_num:
        max_num = last_num
    n = n // 10
print(f"Max number in numbers - {max_num}")
