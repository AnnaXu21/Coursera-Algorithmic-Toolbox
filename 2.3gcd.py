# Uses python3
# import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

# if __name__ == "__main__":
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
#     print(gcd_naive(a, b))


#fast method
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

a = int(input())
b = int(input())
print(gcd_naive(a, b),gcd_fast(a, b))


# stress_test
# from random import randint

# def gcd_stress(a, b):
#     while True:
#         a = randint(1, 100000)
#         b = randint(1, 100000)
#         result1 = gcd_naive(a, b)
#         result2 = gcd_fast(a, b)
#         if result1 == result2:
#             print('OK',result1,result2)
#         else:
#             print('Wrong answer:',result1,result2)
# gcd_stress(2, 8)
   
