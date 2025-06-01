year = int(input())

# year = invalid => 0 >= 0 and > 100000

if year <= 0 or year > 100000:
    print("INVALID")
else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100):
        print("YES")
    else:
        print("NO")
