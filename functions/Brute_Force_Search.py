# Nのものから自由に選ぶ合計や組み合わせなどを全探索する

n= 4
cnt = 0
for i in range(1 << n):
    cond = [0]*n
    for j in range(n):
        if 1 & (i >> j):
            cond[j] = 1
    cnt += 1 
    print(cond)
print(1 >> n)
print(cnt)