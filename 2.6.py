import sys
def fsum1(n):
    a, b = 0, 1
    for i in range((n + 2) % 60):
        a, b = b, (a + b) % 10
    return 9 if a == 0 else a - 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fsum1(n))

