# -*- coding: utf-8 -*-
#fast method
import sys
def gcd_fast(a, b):
    if (a == 0) or (b == 0):
        d = max(a, b)
    elif a == b:
        d = a
    else:
        while (a != 0) and (b != 0):
            if a > b:
                a = a % b          
            else: 
                b = b % a
        d = max(a, b)
    return d

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_fast(a, b))