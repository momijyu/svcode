a, b, c, d = map(int,input().split())
#bからcを比べればいいってこと？
#a,dの場合もあるやんバカ、いもす法か、、、
Imo = [0] * 101
for j in range(a, b+1):
    Imo[j] += 1
for j in range(c, d+1):
    Imo[j] += 1
cnt = Imo.count(2)
if cnt != 0:
    print(cnt-1)
else:
    print(cnt)