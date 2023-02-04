# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print()
print("Данная программа составит список простых множителей числа, которое задаст пользователь.")

print()
n = int(input("Введите число: "))
print()

user_list = []

result = n
divider = 2

while result > 1:
    if result % divider == 0:
        result = int(result/divider)
        user_list.append(divider)
        divider = 2
    else:
        divider += 1

count = 0
len_list = len(user_list)

print("Число", n, "разложенное на простые множители: ", end = "")
for i in user_list:
    if count == len_list - 1:
        print(user_list[count])
    else:
        print(user_list[count], end = "*")
        count += 1