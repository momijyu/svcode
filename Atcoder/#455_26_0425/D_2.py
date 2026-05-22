n, q = map(int,input().split())
dow= [0]*(n+1)
ans= [1]*(n+1)
top= list(range(n+1))
root= list(range(n+1))
pos = [0]*(n+1)
for i in range(q):
    c, p  = map(int,input().split())
    r_c = root[c]
    r_p = root[p]

    move = ans[r_c] - (pos[c]-1)

    x = dow[c]
    if x != 0:
        top[r_c] = x
    else:
        top[r_c] = 0
    dow[c] = p
    top[r_p] = top[r_c]
    pos[c] = ans[r_p] + 1
    ans[r_c] -= move
    ans[r_p] += move
    root[c] = r_p
print(*(root[1:]))