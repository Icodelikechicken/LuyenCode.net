a, symbol, b = input().strip().split()

a = float(a)
b = float(b)

if symbol == "+":
    print(f'{round(a + b, 2):.2f}')
elif symbol == "-":
    print(f'{round(a - b, 2):.2f}')
elif symbol == "*":
    print(f'{round(a * b, 2):.2f}')
else:
    try:
        print(f'{round(a / b, 2):.2f}')
    except:
        print("Math Error")