def increasing(n):
    if n == 0:
        return
    else:
        increasing(n - 1)
        print(n)


n = int(input())
increasing(n)
