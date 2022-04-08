from ctypes import sizeof
import time
import matplotlib.pyplot as plt

# Exercice 1 :

points = []
tab_n = [1, 2, 5, 10, 15, 20, 25,26,27, 28,29 ,30,31]

def ToH(n , A, B, C):
    if n==1:
        return 
    ToH(n-1, A, C, B)
    ToH(n-1, C, B, A)


def graph():          
    for i in tab_n:
        start = time.time()
        ToH(i, 'A', 'B', 'C')
        stop = time.time()
        temps = stop-start
        print(i,temps)
        points.append(temps)
    plt.plot(tab_n, points)
    plt.show()

#graph()

# Exercice 2
def suiteIter(n):
    un1 = 1
    un2 = 1
    start = time.time()
    for i in range (1,n):
        r = un1 + un2
        un2 = un1
        un1= r
    stop = time.time()
    temps = stop - start
    print(temps)
    return r

def suiteRecur(n):
    if n==1 or n == 0 :
        return 1
    else:
        return suiteRecur(n-1)+suiteRecur(n-2)

def timer(n):
    start = time.time()
    suiteRecur(n)
    stop = time.time()
    temps = stop - start
    print(temps)

#timer(43)

# Exercice 3

def cribleErathostene(A,n):
    start = time.time()
    for i in range (2,n):
        if (A[i] != -1) :
            for j in range (i+1, n):
                if A[j] % A[i] == 0 :
                    A[j] = -1
    stop = time.time()
    temps = stop - start
    print(temps)
    return A

A = []

def initA(A,n):
    for i in range(0,n) :
        A.append(i)
    return A

n = 50000
A = initA(A,n)
cribleErathostene(A,n)






