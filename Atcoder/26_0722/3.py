n = int(input())
a = []
for i in range(n):
    ai = int(input())
    a.append(ai)
sa = sorted(a,reverse=True)
ma_1= sa[0]
ma_2= sa[1]
if ma_1 == ma_2:
    for i in range(n):
        print(ma_1) 
    exit()
for i in range(n):
    if a[i] == ma_1:
        print(ma_2)
    else:
        print(ma_1)
