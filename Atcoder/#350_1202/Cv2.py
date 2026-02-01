n = int(input())
a = list(map(int,input().split()))
l = []
count = 0
for i in range(n):
    if i+1 > a[i]:
        l.append([a[i], i+1])
        count += 1
print(count)
for i in l:
    print(*i)