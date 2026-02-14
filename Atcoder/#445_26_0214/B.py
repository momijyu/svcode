n = int(input())
m = []
mlen = 0
for i in range(n):
    s = str(input())
    m.append(s)
    if mlen < len(s):
        mlen = len(s)
for i in range(n):
    dtcnt = (mlen-len(m[i]))//2
    print("."*dtcnt+ m[i] +"."*dtcnt)