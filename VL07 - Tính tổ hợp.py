def giaithua(n):
    tich = 1
    for i in range(2, n + 1):
        tich *= i
    return tich

n, k = map(int, input().strip().split())

print(int(giaithua(n) / giaithua(k) / giaithua(n - k)))
