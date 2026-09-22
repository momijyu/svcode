from collections import deque
h, w, k = map(int,input().split())
grid = [input() for _ in range(h)]
h_bom = [False]* h
w_bom = [False]* w
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            h_bom[i] = True
            w_bom[j] = True
dist = [[-1] * w for _ in range(h)]
queue = deque()
#print(h_bom, w_bom)
for i in range(h):
    for j in range(w):
        if h_bom[i] or w_bom[j]:
            continue
        if grid[i][j] == ".":
            dist[i][j] = 0
            queue.append((i,j))
#print(queue)
while queue:
    x, y = queue.popleft()
    if dist[x][y] == k:
        continue
    for dx, dy in [(1, 0),(-1, 0),(0, 1),(0, -1)]:
        nowx = x + dx
        nowy = y + dy
        if 0 <= nowx < h and 0 <= nowy < w:
            if grid[nowx][nowy] == "." and dist[nowx][nowy] == -1:
                dist[nowx][nowy] = dist[x][y] + 1
                queue.append((nowx, nowy))
                #print(dist)
#print(dist)
ans = 0
for i in range(h):
    for j in range(w):
        if dist[i][j] != -1:
            ans += 1
print(ans)