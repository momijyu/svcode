n, l, r = map(int,input().split())
m = list(range(1,n+1))
ans = m[:l-1]+m[l-1:r][::-1]+m[r:]
for i in range(n):
    print(ans[i], end = " ")