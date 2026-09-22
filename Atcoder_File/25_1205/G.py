n = int(input())
x = list(map(int, input().split()))
p = list(map(int,input().split()))
q = int(input())
for i in range(q):
    sum = 0
    l, r = map(int,input().split())
    for j in range(l, r+1):
        if j in x:
            sum += p[x.index(j)]
    print(sum)