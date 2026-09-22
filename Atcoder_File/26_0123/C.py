n = int(input())
a = list(map(int,input().split()))
cnt = 0
while sum(a) != max(a):
    a.sort()
    a.reverse()
    a[0] -= 1
    a[1] -= 1
    cnt += 1
print(cnt)