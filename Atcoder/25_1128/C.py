n, a= map(int,input().split())
t = list(map(int,input().split()))
sum_time = 0
for i in range(n):
    if sum_time < t[i]:
        sum_time = t[i]
    sum_time += a
    print(sum_time)