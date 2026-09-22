n = int(input())
mid = 998244353
ans = 0
for i in range(1, n+1):
    de = 10**(len(str(i)) - 1)
    cnt = i - de + 1
    ans += cnt 
print(ans % mid)