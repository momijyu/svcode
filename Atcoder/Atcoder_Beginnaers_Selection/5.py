n=3
cnt = 0
for i in range(1 << n):
    cond = [0]*n
    for j in range(n):
        if 1 & (i >> j):
            cond[j] = 1
    cnt += 1 
    print(cond)
