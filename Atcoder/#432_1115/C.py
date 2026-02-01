def prnd(b, d):
    for i in b:
        print(i *d, end= " ")
    print()

n, x, y = map(int,input().split())
a = list(map(int,input().split()))
b = [] 
d = y - x 
e = []
for i in range(n):
    b.append(a[i]-a[0])
prnd(b,d)
print(b)