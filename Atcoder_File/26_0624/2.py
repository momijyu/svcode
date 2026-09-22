a, b, c, d = map(int,input().split())
if c *d <= b:
    print(-1)
else:
    print((a+(c*d -b)-1) //(c*d -b))
