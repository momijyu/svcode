x, y, l, r, a, b = map(int,input().split())
ans = 0
for i in range(a+1, b+1):
    if l < i <= r:
        ans += x
    else:
        ans += y
print(ans)