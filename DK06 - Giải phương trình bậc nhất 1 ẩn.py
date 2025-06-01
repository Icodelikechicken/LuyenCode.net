def main():
    a, b = map(int, input().strip().split())

    if a == 0:
        if b == 0:
            print("WOW")
        else:
            print("NO")
    else:
        print(round(-b/a, 2))

if __name__ == "__main__":
    main()