s = input()
ima = s[0]
ans = 0
for i in range(len(s)):
    if ima != s[i]:
        ans += 1
        ima = s[i]
print(ans)