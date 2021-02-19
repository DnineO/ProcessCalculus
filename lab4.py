import math
#Задание 114 з)

P = 1
for i in range(2,11,1):
    P *= (1 - (1/math.factorial(i))) ** 2
    print(P)
print("Результат = ", P)