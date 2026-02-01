h,w,x,y = map(int,input().split())
s = []
x -= 1
y -= 1
count = set()
for _ in range(h):
    s.append(input())
t = str(input())
for i in range(len(t)):
    bx, by = x,y
    if t[i] == "U":
        bx -= 1
    elif t[i] == "D":
        bx += 1
    elif t[i] == "L":
        by -= 1
    else:
        by += 1
    if s[bx][by] != "#":
        x,y = bx,by
        if s[x][y] == "@":
            count.add((x,y))
print(x+1,y+1,len(count))