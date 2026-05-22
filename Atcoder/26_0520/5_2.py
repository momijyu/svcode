n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
# 隣り合う二つを見つける
i = 0
ans = 0
wh = []
while i < n-1:
    if a[i] == a[i+1]:
        wh.append(a[i])
        i += 1
    elif len(wh) >= 2:
        break
    i += 1
if len(wh) >= 2:
    ans = wh[0] * wh[1]
print(ans)