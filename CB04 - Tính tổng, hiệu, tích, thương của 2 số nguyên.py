def main():
    a, b = map(int, input().strip().split())

    print(a + b)
    print(a - b)
    print(a * b)
    print(round(a / b, 2) if b != 0 else "ERROR")

if __name__ == "__main__":
    main()