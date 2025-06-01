index = 0

def main():
    global index

    n = input()

    for i in range(len(n)):
        if n[i] == ".":
            index = i + 1
            break

    a = float(n[0 : index-1])

    if float(n[index]) >= 5:
        if n[0] == "-":
            print(round(a - 1))
        else:
            print(round(a + 1))
    else:
        print(round(a))

if __name__ == "__main__":
    main()