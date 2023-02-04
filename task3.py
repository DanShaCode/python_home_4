# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

print()
n = int(input("Задайте длину последовательности чисел: "))
print()

start_list = []

count = 0

while count < n:
    start_list.append(random.randint(0,5))
    count += 1

print()
print("Созданная последовательность: ", ', '.join(map(str,start_list)))

max = 0

for i in start_list:
    if i > max:
        max = i

counter_len = max + 1
counter = []
count = 0

while count < counter_len:
    i = counter.append(0)
    count += 1

for i in start_list:
    counter[i] += 1

uniqe_list = []

count = 0
number = 0

for i in counter:
    if i != 0:
        uniqe_list.append(number)
        number += 1
    else:
        number += 1
        continue

print()
print("Список неповторяющихся элементов исходной последовательности", ', '.join(map(str,uniqe_list)))