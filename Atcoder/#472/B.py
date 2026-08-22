n = int(input())
l = list(map(int,input().split()))
maxl = sum(l)
nowl = 0
minl = sum(l)
for i in l:
    nowl += i 
    maxl -= i
    d = abs(nowl - maxl)
    if minl > d:
        minl = d
print(minl)