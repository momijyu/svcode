n, m = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
dis = [] 
for i in range(m-1):
    dis.append(x[i+1] - x[i])
print(x,dis)
diss = sorted(dis)
