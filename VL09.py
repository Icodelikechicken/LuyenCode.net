
def giaithua(n):
    tich = 1
    for i in range(2, n + 1):
        tich *= i
    return tich

x, n = map(int, input().strip().split())

tong = 0

for i in range(1, n + 1):
    tong += (x ** i) / giaithua(i)

print(f'{tong:.2f}')