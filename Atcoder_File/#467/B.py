n = int(input())
ans = 0
for i in range(n):
    a, b, c = map(str,input().split())
    if c == "keep":
        ans += int(b)-int(a)
print(ans)