def check(x):
    count = 0
    now_r = -10**18  
    for L, R in lr:
        if L >= now_r + x:
            count += 1
            now_r = R  
    return count >= k

n, k = map(int,input().split())
lr = []
for i in range(n):
    li, ri = map(int,input().split())
    lr.append((li, ri))
#print(lr)
lr.sort(key=lambda x:x[1])
ok= 0
ng= 10 **18
while ng - ok > 1:
    mid = (ok + ng) //2
    if check(mid):
        ok = mid 
    else:
        ng = mid 

if ok == 0:
    print(-1)
else:
    print(ok)
