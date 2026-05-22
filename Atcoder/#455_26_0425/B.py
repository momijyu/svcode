h, w = map(int,input().split())
grid = []
for i in range(h):
    grid.append(input())
ans = 0
for i1 in range(h):
    for i2 in range(i1,h):
        for j1 in range(w):                     
            for j2 in range(j1,w):
                check = True
                for i in range(i1,i2+1):
                    for j in range(j1,j2+1):
                        ni = i1 + i2 - i
                        nj = j1 + j2 - j
                        if grid[i][j] != grid[ni][nj]:
                            check = False
                            break
                    if not check:
                        break
                if check:
                    ans += 1
print(ans)