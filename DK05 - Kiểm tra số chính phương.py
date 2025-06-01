# Chinh phuong => la so nguyen > 0 và căn bậc 2 của nó là 1 số nguyên

def main():
    n = int(input())

    print("YES" if n > 0 and (n ** 0.5) == int(n ** 0.5) else "NO")

if __name__ == "__main__":
    main()