n, m = map(int, input().split())
x = [0] * m
y = [0] * m
for i in range(m):
    x[i], y[i] = list(map(int,input().split()))
print(x, y)