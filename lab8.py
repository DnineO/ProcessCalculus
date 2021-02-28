import numpy as np
# 677б

n = 3
a = np.ones((n, n))
b = np.zeros((n, n))
print(b)

for i in range(n):
    for j in range(n):
        tmp = 0
        for k in range(i + 1):
            b[i, j] += np.sum(a[k][j])

print(b)