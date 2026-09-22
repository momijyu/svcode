n, q = map(int,input().split())
a = list(map(int,input().split()))
A = []
for i in range(n):
    A.append((a[i], i+1))
A.sort()
top = A[:6]
print(top)
for i in range(q):
    k = int(input())
    b = list(map(int,input().split()))
    rm = set(b)
    for val, idx in top:
        if idx not in rm:
            print(val)
            break