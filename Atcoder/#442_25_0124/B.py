q = int(input())
m = 0
st = False
for i in range(q):
    a = int(input())
    if a == 1:
        m += 1
    elif a == 2:
        if m >= 1:
            m -= 1
    elif a == 3:
        if st:
            st = False
        else:
            st = True 
    if st and m >= 3:
        print("Yes")
    else:
        print("No")