# -*- coding: utf-8 -*-


# fast method
def fib(n):
    if (n <= 1):
        return n
    else:
        Arr = [0, 1]
        for i in range(n):
            Arr[i] = Arr[i-1] + Arr[i-2]
            Arr.append(Arr[i])
        return Arr[n]
n = int(input())
print(fib(n))
