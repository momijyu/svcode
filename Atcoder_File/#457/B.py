n = int(input())
l = []
for i in range(n):
    le = list(map(int,input().split()))
    l.append(le)
x, y = map(int,input().split())
print(l[x-1][y])