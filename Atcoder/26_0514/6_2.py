n = int(input())
mid = 998244353
ans = 0
l = 1
while l <= n:
    r = min(l * 10 - 1, n)
    m = r -l + 1
    ans += m * (m + 1) // 2
    l *= 10
print(ans % mid)