n = int(input())
a = list(map(int,input().split()))
s = set()
count = 0
for i in range(n):
    if a[i] not in s:
        s.add(a[i])
        num = a.count(a[i])
        count += num * (num -1) //2 * (n - num)
print(count)
