def Euler(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().strip().split())

a = abs(a)

b = abs(b)

print(Euler(a, b))