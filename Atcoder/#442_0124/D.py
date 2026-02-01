def sum(a,s,e):
    sum = 0
    for i in range(s,e+1):
        sum += a[i]
    return sum 

n, q = map(int,input().split())
a = list(map(int,input().split()))
for i in range(q):
    x = list(map(int,input().split()))
    if x[0] == 1:
        baf = a[x[1]-1]
        a[x[1]-1] = a[x[1]]
        a[x[1]] = baf
    else:
        print(sum(a,x[1]-1,x[2]-1))
