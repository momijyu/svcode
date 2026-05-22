n = int(input())
t, a = map(int,input().split())
h = list(map(int,input().split()))
ans = float('inf')
ans_idx = 0
for i in range(n):
    he = t - h[i] * 0.006
    if abs(a - he) < ans:
        ans = abs(a - he)
        ans_idx = i+1
print(ans_idx)