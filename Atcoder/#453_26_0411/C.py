n = int(input())
l = list(map(int,input().split()))
ans = 0
for i in range(2**n):
    place = 0.5
    cnt = 0
    for j in range(n):
        if (i>>j) & 1:
            n_place = place + l[j]
        else:
            n_place = place - l[j]
        if place * n_place < 0:
            cnt += 1
        place = n_place
    ans = max(ans, cnt)

print(ans)