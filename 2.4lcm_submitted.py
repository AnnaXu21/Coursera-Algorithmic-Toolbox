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

def lcm_fast(a, b):
    if a == b:
        return a
    elif max(a, b) % min(a, b) == 0:
        return max(a, b)
    else:
        d = gcd_fast(a, b)
    return a*b//d

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

# a = int(input())
# b = int(input())
# print(lcm_fast(a, b))
