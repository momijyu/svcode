h, w = map(int,input().split())
grid = ['.' * w for _ in range(h)]
for i in range(1,h -1):
    grid[i] = "#"+'.'*(w-2)+"#"
    grid[i] = "#"+'.'*(w-2)+"#"
grid[0] = '#'*w
grid[h-1] = '#'*w
for i in range(h):
    print(grid[i])