t = int(input())
for i in range(t):
    x, y, k = map(int,input().split())
    cnt = 0
    while True:
        if x == y:
            print(cnt)
            break
        if x > y:
            x //= k
        elif x < y:
            y //= k
        cnt += 1
