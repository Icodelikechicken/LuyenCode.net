def KTHOANHAO(n):
    sum = n
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            sum -= i
    return sum

n = int(input())
# print(KTHOANHAO(n))
print("YES" if KTHOANHAO(n) == 0 else "NO")