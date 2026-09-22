n, k = map(int,input().split())
a = list(map(int,input().split()))
s = set(a % k for a in a)
b = sorted(list(s))
ans = b[-1] - b[0]
for i in range(1, len(b)):
    diff = b[i-1]+ k - b[i]
    if diff < ans:
        ans = diff
print(ans)