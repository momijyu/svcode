n, q= map(int,input().split())
x= []
for i in range(q):
    x += map(int,input().split())
l= []
for i in range(n):
    l.append(i+1)
nu= 1
count= 0
for j in x[::2]:
    for i in range(n):
        if l[i] <= j:
            l[i]= x[nu]
            count += 1
    print(count)
    count= 0
    nu += 2


        