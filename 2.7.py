# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 22:39:17 2022

@author: Mengxin
"""

import sys
def fsum(n):
    a, b = 0, 1
    for i in range((n + 2) % 60):
        a, b = b, (a + b) % 10
    return 9 if a == 0 else a - 1

def fsump(m, n):
    result = fsum(n) - fsum(m-1)
    return result % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fsump(from_, to))
