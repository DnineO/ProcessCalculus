import random

# Данные натуральные числа n,q1,...,qn. найти те члены qi последовательности q1,...,qn, которые
# a) являются удвоенными нечетными числами;

n = 10
a = []

for i in range(n):
    a.append(random.randint(1, 19))
    print(a[i])

for i in range(n):
    if a[i] 