from collections import Counter

n = int(input())
a = list(map(int,input().split()))
ca = Counter(a)
print(ca)
ans = 0
for x, cnt in ca.items():
    #print(x, cnt)
    if x <= cnt:
        ans += min(cnt-x, cnt)
    else:
        ans += cnt
print(ans)