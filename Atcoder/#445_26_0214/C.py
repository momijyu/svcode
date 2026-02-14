n = int(input())
a = list(map(int,input().split()))
data = [-1] * n
for i in range(n):
    now = i
    path = []
    while now+1 != a[now] and data[now] == -1:
        path.append(now)
        now = a[now]-1
    if data[now] != -1:
        ans = data[now]
    else:
        ans = now
    data[now] = ans
    for j in path:
        data[j] = ans
    print(ans+1, end = " ")
