def UCLN(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# Này là công thức Euler thì phải

a, b = map(int, input().strip().split())

if b == 0:
    print("INVALID")

else:
    print(f'{int(a/UCLN(a, b))} {int(b/UCLN(a,b))}' if a % b else f'{int(a/b)}')