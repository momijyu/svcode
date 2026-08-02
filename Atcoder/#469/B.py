n = int(input())
s = str(input())
ans = 0
if n == 1:
    if s[0] == "x":
        print(1)
        exit()
    else:
        print(0)
        exit()
if [s[0], s[1]] == ["x","x"]:
    ans += 1
if [s[-1],s[-2]] == ["x", "x"]:
    ans += 1
for i in range(1, n-1):
    if [s[i-1], s[i], s[i+1]] == ["x","x","x"]:
        ans += 1
print(ans)