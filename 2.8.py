# -*- coding: utf-8 -*-

import sys
def fib_last_digit(n):
    if n <= 1:
        return n
    else:
        a = 0 
        b = 1
        n = n % 60
        for i in range(n - 1):
            c = a + b
            c = c % 10
            a, b = b, c
    return c

def sqsum(n):
    result = fib_last_digit(n) * fib_last_digit(n+1)
    return result % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(sqsum(n))