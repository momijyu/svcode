from bisect import bisect_left, bisect_right
n, q = map(int,input().split())
a= list(map(int,input().split()))
a.sort()
z= []
for i in range(q):
    x, y = map(int,input().split())
    cnt = 0
    gp = x+y-1
    in_a = bisect_left(a,x)
    cnt_gp_high= bisect_right(a,gp)
    while cnt_gp_high != in_a+cnt:
        cnt = cnt_gp_high-in_a
        gp += 1 
        cnt_gp_high= bisect_right(a,gp)