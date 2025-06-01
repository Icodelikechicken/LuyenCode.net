# Bài này đang sai vài test :>>>
# Xét thêm trường hợp các phần tử bằng 0

#  ax2 + bx + c = 0

def pt_bac_2(a, b, c):
    
    if a == 0:
        if b == 0:
            if c == 0:
                print("WOW")
                return
            else:
                print("NO")
                return
        else:
            x = round(-c/b, 2)
            print(x)
            return

    else:
        delta = b * b - (4 * a * c)

        if delta < 0:
            print("NO")
            return
        elif delta == 0:
            x = -b / (2 * a)
            print(round(x, 2))
            return
        else:
            x1 = (-b - delta ** 0.5) / (2 * a)
            x2 = (-b + delta ** 0.5) / (2 * a)
            print(round(min(x1, x2), 2), round(max(x1, x2), 2))
            return


def main():
    a, b, c = map(float, input().strip().split())
    pt_bac_2(a, b, c)

if __name__ == "__main__":
    main()

    # OK


    