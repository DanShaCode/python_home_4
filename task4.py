# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

print()
k = "**"+input("Введите, пожалуйста, степень k: ")

rand_coff = random.randint(3, 3)

coff = []

iter = rand_coff
count = 0

while count < iter:
    coff.append(random.randint(0, 100))
    count += 1

plus = '+'
minus = '-'
symbol = 0

coff_elements = len(coff) 
number_of_symbols = coff_elements - 1

count = 0

symbols = []

while count < number_of_symbols:
    flag = random.randint(0,1)
    if flag == 0:
        symbols.append(minus)
        count += 1
    if flag == 1:
        symbols.append(plus)
        count += 1

coff_elements = len(coff) 

count = 0
border = coff_elements + number_of_symbols

formula = []

while count < border:
    if count % 2 == 0:
        formula.append(coff[random.randint(0, coff_elements - 1)])
        count += 1
    else:
        formula.append(symbols[random.randint(0, number_of_symbols - 1)])
        count += 1

unknown = ['x', 'y']
randomizer = random.randint(0,1)

count = 0
border = coff_elements
index = 1

while count < border:
    formula.insert(index, unknown[randomizer])
    count += 1
    index += 3

count = 0
index = 2

while count < border:
        i = formula.insert(random.randrange(2, 8, 3), k)
        count += 1
        index += 3
        break


print()
print("Созданная формула: ", *formula, "= 0", end = "")
print()