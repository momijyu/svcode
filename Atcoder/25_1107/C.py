n = int(input())
a = list(map(int,input().split()))
count = 0
while a.count(0) < len(a)-1:
    a.sort()
    a.reverse()
    a[0] -= 1
    a[1] -= 1
    count += 1
print(count)