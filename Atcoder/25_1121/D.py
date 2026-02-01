import math
x, y, d = map(int,input().split())
x2= x * math.cos(math.radians(d))-y*math.sin(math.radians(d))
y2= x * math.sin(math.radians(d))+y*math.cos(math.radians(d))
print(x2, y2, sep = " ")