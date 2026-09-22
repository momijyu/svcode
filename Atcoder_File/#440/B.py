n = int(input())
t = list(map(int,input().split()))
t2= t.copy()
t2.sort()
ans = []
for i in range(3):
    a= t.index(t2[i])
    ans.append(a+1)
print(*ans)