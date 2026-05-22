n, q = map(int,input().split())
up = [0]*(n+1)
dow= [0]*(n+1)
ans= [0]*(n+1)
top= list(range(n+1))
root= list(range(n+1))
c, p = [], []
for i in range(q):
    c, p  = map(int,input().split())
    x = dow[c]
    if x != 0:
        up[x] = 0
    dow[c] = p
    up[p] = c
ans = [0]*(n+1)
for i in range(1,n+1):
    b = i
    while dow[b] != 0:
        b = dow[b]
    ans[b] += 1
print(*(ans[1:]))