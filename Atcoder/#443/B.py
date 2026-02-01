n, k  = map(int,input().split())
sum = n
n += 1
cnt = 0
while sum < k:
    sum += n
    n += 1
    cnt += 1
print(cnt)