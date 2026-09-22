N = int(input())
L = []
m = set()
for i in range(N):
    a = list(map(int,input().split()))
    a = tuple(a)
    m.add(a)
print(len(m))