n = int(input())
a = list(map(int,input().split()))
o = 0
t = 0
h = 0
for i in a:
    b = i % 10
    if b != 0:
        o += 10-b
        i -= b
        i += 10
    b = i % 100
    if b != 0:
        t += 10 - (b//10)
        i -= b
        i += 100
    b = i % 1000
    if b != 0:
        h += 10 - (b//100)
print(o, t, h)