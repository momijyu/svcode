t = int(input())
for i in range(t):
    n, d = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    b_cnt= 0
    egg_cnt= 0
    lost_egg= 0
    z= 0
    for j in range(n):
        egg_cnt += a[j]
        egg_cnt -= b[j]
        b_cnt += b[j]
        if j > d-1:
            lost_egg = a[z]
            if b_cnt < lost_egg:
                egg_cnt -= a[z]-b_cnt
            z+= 1
    print(egg_cnt)