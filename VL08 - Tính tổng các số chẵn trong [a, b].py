a, b = map(int, input().strip().split())

tong = 0

for i in range(a, b + 1):
    tong += i if i % 2 == 0 else 0

print(tong)