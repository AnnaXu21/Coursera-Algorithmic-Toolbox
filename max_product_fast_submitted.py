# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:20:55 2022

@author: Mengxin
"""

# faster method
def max_product_fast(numbers):
    n = len(numbers)
    first = 0
    for i in range(n):
        if numbers[i] > numbers[first]:
             first = i
    if first == 0:
        second = 1
    else: 
        second = 0
    for j in range(n):
         if j != first and numbers[j] > numbers[second]:
              second = j
    return numbers[first] * numbers[second]
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_product_fast(input_numbers))
