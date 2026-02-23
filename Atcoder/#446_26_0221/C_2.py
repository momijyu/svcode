t = int(input())
for i in range(t):
    n, d = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    egg= 0
    z= 0
    for j in range(n):
        a[z] -= b[j]
        if a[z] < 0:
            idx = z
            while a[idx] < 0:
                a[idx+1] += a[idx]
                idx +=1
        if j > d-1:
            a[z]= 0
            z+= 1
    print(sum(a))