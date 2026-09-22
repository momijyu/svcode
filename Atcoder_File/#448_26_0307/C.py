n, q = map(int,input().split())
a = list(map(int,input().split()))
A = []
for i in range(1, n+1):
    A.append((a[i-1], i))
A.sort()
top_6 = A[:6]
for i in range(q):
    k = int(input())
    b = list(map(int,input().split()))
    rm = set(b)
    for v, idx in top_6:
        if idx not in rm:
            print(v)
            break