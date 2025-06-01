month, year = map(int, input().split())

a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]

if month < 1 or month > 12 or year < 0 or year > 100000:
    print("INVALID")
else:
    if month in a:
        print(31)
    elif month in b:
        print(30)
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100):
            print(29)
        else:
            print(28)