n = int(input())
w = []
x = []
ans = [0] * 24
for i in range(n):
    wi, xi = map(int, input().split())
    w.append(wi)
    x.append(xi)
for i in range(24):
    for j in range(len(w)):
        if 9 <= (x[j] + i) % 24 < 18:
            ans[i] += w[j]
print(max(ans))