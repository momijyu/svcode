n = int(input())
a = list(map(int,input().split()))
col = [True] * 9
cnt = [0] * 9
for i in range(n):
    s = a[i] // 400
    if s >= 8:
        cnt[8] += 1
    else:
        if col[s]:
            col[s] = False
            cnt[s] += 1
ans = 0
for i in range(8):
    if col[i]:
        ans += 1
if cnt[8] > 0:
    print(max(ans,1), ans + cnt[8])
else:    
    print(ans, ans)

