h,w = map(int,input().split())
grid = [list(input()) for _ in range(h)]
#print(grid)
l,r,u,d = w-1, 0, h-1, 0
check = False
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            check = True
            if l > j:
                l = j
            if r < j:
                r = j
            if u > i:
                u = i
            if d < i:
                d = i
            #print(l,r,u,d)
for i in range(u, d + 1):
    print("".join(grid[i][l : r + 1]))
