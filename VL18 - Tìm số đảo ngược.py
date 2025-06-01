n = input()

# n = n[::-1]  Đây là cách để lật mảng lại

n = n[::-1]

while n[0] == '0':
    n = n[1::]

print(n)