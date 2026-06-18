n = int(input())
s = input()
rcnt = 0
for i in s:
    if i == "R":
        rcnt += 1
#print(rcnt)
ans = 0
for i in range(rcnt):
    if s[i] == "W":
        ans += 1
print(ans)