q = int(input())
l = []
for i in range(q):
    a = list(map(int,input().split()))
    if a[0]== 1:
        l.append(a[1])
    elif a[0] == 2:
        print(l[len(l)-a[1]])