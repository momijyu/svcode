from collections import deque

n = int(input())
s = str(input())
ans = deque()
rever = False

for i in range(n):
    if rever:
        ans.appendleft(i + 1)
    else:
        ans.append(i + 1)
        
    if s[i] == 'o':
        rever = not rever
if rever:
    ans.reverse()
print(*ans)