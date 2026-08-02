n, m = map(int,input().split())
ans = [-1]*n
se = set()
for i in range(m):
    si ,ci = map(int,input().split())
    if ans[si-1] != -1  and ans[si-1] != ci:
        print(-1)
        exit()
    ans[si-1] = ci

if n == 1:
    if ans[0] == -1:
        print(0)
    else:
        print(ans[0])
    exit()
if ans[0] == 0:
    print(-1)
    exit()
#print(ans)
for i in range(n):
    if ans[i] == -1:
        if i == 0:
            print(1, end= "")
        else:
            print(0,end= "")
    else:
        print(ans[i], end= "")
