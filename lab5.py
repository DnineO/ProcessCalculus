import random
#Задание 136 к)

n = 10
a = []
summ = 0

for i in range(n):
    a.append(random.randint(-10,10))
    print(a[i])
    summ += a[i]

print("Summ = ",summ)
print("Result = ",2 * summ**2)