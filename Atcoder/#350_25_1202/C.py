def change(a, x, y):
    buf = a[x]
    a[x] = a[y]
    a[y] = buf

n = int(input())
a = list(map(int,input().split()))
l = []
count = 0
for i in range(n-1):
    if a[i] != i:
        for j in range(i+1,n):
            if a[j] == i+1:
                b = [i+1, j+1]
                l.append(b)
                change(a,i,j)
                count += 1
print(count)
for i in l:
    print(*i)