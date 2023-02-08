# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

print()
print("Данная программа считывает информацию из двух файлов, которые содержат многочлен.")
print()
print("Далее программа формирует новый файл, содержащий сумму многочленов.")

first_polynomial = []
second_polynomial = []

with open('task5(1).txt') as f:
    first_polynomial = list(map(str, f.read().split()))

with open('task5(2).txt') as f:
    second_polynomial = list(map(str, f.read().split()))

polynomial_sum = [] 

for i in first_polynomial:
    if i == str(0):
        first_polynomial.remove(i)
   
for i in first_polynomial:
    if i == '=':
        first_polynomial.remove(i)
    else:
        polynomial_sum.append(i)

for i in second_polynomial:
    if i == str(0):
        second_polynomial.remove(i)

for i in second_polynomial:
    if i == '=':
        second_polynomial.remove(i)
    else:
        polynomial_sum.append(i)

print()
print("Сумма многочленов записана в файле task5.txt")
file = open("task5(result).txt", "w")
file.write("Сумма многочленов: ")
file.write(''.join(map(str,first_polynomial)))
file.write(" + ")
file.write(''.join(map(str,second_polynomial)))
file.write(" = ")
file.write("0 ")
file.close()