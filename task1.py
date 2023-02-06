print()
print("Данная программа находит число П c заданной точностью d.")
print()
print("При условии, что 10^(-1) ≤ d ≤ 10^(-10).")
print()
d = input("Задайте число d сюда ---> ")
print()

if float(d) < (10**-1) and float(d) > (10**-10) or float(d) == (10**-1) or float(d) == (10**-10):
    count_numbers_after = - 1

    for i in d:
        if i != ".":
            count_numbers_after += 1

    if count_numbers_after == 0:
        print(3)
    else:
        iterations = 100000
        count = 0
        denominator_num = 3
        result = 4

        while count < iterations:
            if count == 0 or count % 2 == 0:
                result = result - (4/denominator_num)
                denominator_num += 2
                count += 1
            else:
                result = result + (4/denominator_num)
                denominator_num += 2
                count += 1

        result = str(result)

        count = 0
        numbers_after = 2 + count_numbers_after

        print("Число Пи с точностью", count_numbers_after, "знака(ов) после запятой: ", end = "")
        for i in result:
            print(i, end = "")
            count += 1
            if count == numbers_after:
                break

    print()
else:
    print("Число d не соответствует условиям задачи.")