q = int(input())
L = []
for i in range(q):
    a,b=list(map(int,input().split()))
    if a == 1:
        L.append(b)
    else:
        print(L[-b])