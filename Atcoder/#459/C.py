n, q = map(int,input().split())
bl = [0]* n
for i in range(q):
    x, y = map(int,input().split())
    cnt = 0
    if x == 1:
        bl[y-1] += 1
    else:
        for j in range(n):
            if bl[j] >= y + min(bl):
                cnt += 1
        print(cnt)