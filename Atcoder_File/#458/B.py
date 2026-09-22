h, w = map(int,input().split())
for i in range(1, h +1):
    ans = []
    for j in range(1, w +1):
        cnt = 0
        if i > 1: cnt += 1
        if i < h: cnt += 1
        if j > 1: cnt += 1
        if j < w: cnt += 1
        ans.append(str(cnt))
    print(" ".join(ans))