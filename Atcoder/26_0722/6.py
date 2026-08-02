n = int(input())
s = []
sa = 0
for i in range(n):
    a, b = map(int,input().split())
    s.append((a+b, a))
    sa += a
s.sort(reverse=True)
#print(s,sa)
sb = 0
cnt = 0
while True:
    if sb > sa:
        break
    sb += s[cnt][0]
    sa -= s[cnt][1]
    cnt += 1
print(cnt)