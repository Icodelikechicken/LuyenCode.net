n = int(input())

sum = 0

for i in range(1, 3 * n + 2):
    sum += i if i % 2 else -i

print(sum)