n = int(input())
a = list(map(int,input().split()))
c_odd = 0
c_2 = 0
c_4 = 0
for i in a:
    if i % 2 != 0:
        c_odd += 1
    elif i % 4 == 0:
        c_4 += 1
    else:
        c_2 += 1
if c_2 > 0:
    if c_odd <= c_4:
            print("Yes")
    else:
            print("No")
else:
    if c_odd <= c_4 + 1:
         print("Yes")
    else:
         print("No")