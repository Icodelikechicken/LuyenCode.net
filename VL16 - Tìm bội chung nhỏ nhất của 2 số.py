def UCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().strip().split())

print(int(abs((a * b / UCLN(a, b)))))