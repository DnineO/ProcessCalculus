# Дано натуральное число n. Вычислить:
# сумму k в степени k

n = 4
k = 0

for i in range(n):
    k += pow(i,i)
print(k)