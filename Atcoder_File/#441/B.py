n, m= map(int,input().split())
s= str(input())
ss= set(s)
t= str(input())
st= set(t)
q= int(input())
for i in range(q):
    w= str(input())
    sw= set(w)
    taka= sw.issubset(ss)
    aoki= sw.issubset(st)
    if taka and not aoki:
        print("Takahashi")
    elif not taka and aoki:
        print("Aoki")
    else:
        print("Unknown")