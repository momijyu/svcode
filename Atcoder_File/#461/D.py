from collections import defaultdict
h, w, k = map(int, input().split())
grid = [input() for _ in range(h)]
sum = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(h):
    for j in range(w):
        val = int(grid[i][j])
        sum[i + 1][j + 1] = sum[i + 1][j] + sum[i][j + 1] - sum[i][j] + val
ans = 0
for i in range(h):
    for j in range(i, h):
        cnt = defaultdict(int)
        cnt[0] = 1
        sum_2 = 0
        for l in range(w):
            