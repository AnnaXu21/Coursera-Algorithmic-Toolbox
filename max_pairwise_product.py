# navie method
def max_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

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

from random import randint
def max_prod_stress(N,M):
    while True:
        n = randint(2,N)
        A = [None]*n
        for i in range(n):
            A[i] = randint(0,M)
        print(A)
        result1 = max_product_naive(A)
        result2 = max_product_fast(A)
        if result1==result2:
            print('OK')
        else:
            print('Wrong answer:',result1,result2)
            return
max_prod_stress(5,1000)
