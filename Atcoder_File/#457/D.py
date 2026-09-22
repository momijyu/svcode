def is_pos(x):
    tol_cost = 0
    for i, val in enumerate(a):
        if val < x:
            cost = x - val
            tol_cost += (cost + (i + 1) - 1) // (i + 1)
            if tol_cost > k:
                return False
        #print(tol_cost)
    return True 

n, k = map(int,input().split())
a = list(map(int,input().split()))
min_pos = min(a)
max_pos = max(a) + n *k + 1
while max_pos -min_pos > 1:
    mid = (min_pos + max_pos) //2
    #print(mid)
    if is_pos(mid):
        min_pos = mid
    else:
        max_pos = mid
print(min_pos)
#print(max_pos)