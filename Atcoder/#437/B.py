h, w, n = map(int,input().split())
a = []
for i in range(h):
    ba = list(map(int,input().split()))
    a.append(ba)
ans = [0]*h
for i in range(n):
    b = int(input())
    cnt = 0
    for j in range(h):
        if b in a[j]:
            ans[j] += 1
print(max(ans))