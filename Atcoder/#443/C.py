n, t = map(int,input().split())
a = list(map(int,input().split()))
losstime = 0
chtime = 0
for i in a:
    if losstime <= i:
        chtime +=  i - losstime
        losstime = i + 100
if losstime < t:
    chtime += t - losstime
print(chtime)
