def KTNGUYENTO(n):
    if n < 2:
        return False    
    for i in range(2, int((n**0.5)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
print("YES" if KTNGUYENTO(n) else "NO")