import math
#Задание 114 з)

P = 1
ii =1
for i in range(2,11,1):
    ii = ii * i
    P *= (1 - (1/(ii))) ** 2
    #todo: факториал увеличивать зная предыдущий
    print(P)
print(f"Результат = {P:.5f}")
