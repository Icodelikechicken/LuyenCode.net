n = int(input())

res = set()

n = abs(n)

for i in range(1, n + 1):
    if n % i == 0:
        res.add(i)
        res.add(int(n/i))

if n == 0:
    print("INF")
else:
    for i in sorted(res, reverse = True):
        print(int(i), end = " ")