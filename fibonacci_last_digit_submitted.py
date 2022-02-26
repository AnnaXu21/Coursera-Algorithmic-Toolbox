# -*- coding: utf-8 -*-
# fast method
def fib_last_digit(n):
    if n <= 1:
        return n
    else:
        a = 0 
        b = 1
        for i in range(n - 1):
            c = a + b
            c = c % 10
            a, b = b, c
    return c

if __name__ == '__main__':
    n = int(input())
    print(fib_last_digit(n))