import random

# Данные натуральные числа n,q1,...,qn. найти те члены qi последовательности q1,...,qn, которые
# a) являются удвоенными нечетными числами;

n = 6
a = [9, 25, 14, 49, 81, 121]

for i in range(n):
#      a.append(random.randint(1, 19))
     print(a[i])

print("_____________________________________")
for i in range(n):
    if a[i] % 2 == 0:
        print("не подходит")
    else:
        if a[i] != 3:
            if a[i] % 3 == 0:
                print(a[i], ' ')
        if a[i] != 5:
            if a[i] % 5 == 0:
                print(a[i], ' ')
        if a[i] != 7:
            if a[i] % 7 == 0:
                print(a[i], ' ')
        if a[i] != 9:
            if a[i] % 9 == 0:
                print(a[i], ' ')
        if a[i] != 11:
            if a[i] % 11 == 0:
                print(a[i], ' ')
