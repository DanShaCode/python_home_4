import random

print()
print("Данная программа формирует многочлен степени k.")
print()
print("Степень k задается пользователем.")
print()

k = "**"+input("Введите, пожалуйста, степень k: ")

rand_coff = random.randint(1, 3)

coff = []

iter = rand_coff
count = 0

while count < iter:
    coff.append(random.randint(0, 100))
    count += 1

plus = ' + '
minus = ' - '
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
        formula.insert(len(formula), " = 0")
        count += 1
        index += 3
        break

for i in formula:
    if i == 0:
        formula.remove(0)
    if i == '**0':
        formula.remove('**0')

print()
print("Ответ записан в файле task4.txt")

file = open("task4.txt", "w")
file.write("Сгенерированный многочлен: ")
file.write(''.join(map(str,formula)))
file.close()