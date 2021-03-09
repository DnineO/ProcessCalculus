import random
import numpy as np

def randArr(a,n):
    for i in range(n):
        a.append(random.randint(1, 19))
        print(a[i])

def printArr(a,n):
    for i in range(n):
        print(a[i])

def lab5(a,n):
    summ = 0
    for i in range(n):
        a.append(random.randint(-10, 10))
        print(a[i])
        summ += a[i]
    return summ

def lab6(a,n):
    print("_____________________________________")
    for i in range(n):
        perem = a[i] / 2
        if perem == 3:
            if perem % 3 == 0:
                print(a[i], ' ')
        if perem == 5:
            if perem % 5 == 0:
                print(a[i], ' ')
        if perem == 7:
            if perem % 7 == 0:
                print(a[i], ' ')
        if perem == 9:
            if perem % 9 == 0:
                print(a[i], ' ')
        if perem == 11:
            if perem % 11 == 0:
                print(a[i], ' ')

def lab7(n):
    k = 0
    for i in range(1, n + 1):
        k += i ** i
    print(k)

def lab8(n):
    a = np.ones((n, n))
    b = np.zeros((n, n))
    print(a)
    print(b)
    for i in range(n):
        for j in range(n):
            summ = 0
            for k in range(n - i - 1, n):
                for l in range(n - j - 1,n):
                    summ += a[k][l]
            b[i][j] = summ
    print(b)