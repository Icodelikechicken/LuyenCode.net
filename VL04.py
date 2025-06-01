n = int(input())

sum = 0

for i in range(2, n + 1):
    sum += float(1 / i)

print(f'{round(sum, 4):.4f}')