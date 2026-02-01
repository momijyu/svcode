n = int(input())
grid = [[0] * n for i in range(n)]
grid[0][(n-1)//2]= 1
r, c = 0, (n-1)//2
for i in range(n**2-1):
    if grid[(r-1) % n][(c+1) % n] == 0:
        r, c = (r-1) % n, (c+1) % n
    else:
        r, c = (r+1) % n, c
    grid[r][c] = i + 2
for i in grid:
    print(" ".join(map(str, i)))