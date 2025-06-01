# def gt(n):
#     sum = 1
#     for i in range(2, n + 1):
#         sum *= i
#     return sum

# x, n = map(int, input().strip().split())


# for i in range(1, n + 1):a
#     sum += pow(x, i) / gt(i)

# # print(type(str(sum)))

# print(len(str("{:.2f}".format(sum))))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# n = int(input())

# # uoc = set()
# # n = abs(n)
# sum = 0

# for i in range(1, int(n*0.5) + 1):
#     if n % i == 0:
#         sum += i

# print("YES" if sum == n and n > 0 else "NO")

def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)  # Trả về số dương

a, b = map(int, input().strip().split())

minus = "-" if a * b < 0 else ""

if b == 0:
    print("INVALID")
else:
    print(f"{minus}{int(abs(a/ucln(a,b)))} {int(abs(b/ucln(a,b)))}" if a % b else f"{minus}{int(abs(a/ucln(a,b)))}")
