l = ["Red" ,"Green", "Blue"]
m = list(map(int,input().split()))
c = str(input())
if c == l[0]:
    m[0] = max(m)
    print(min(m))
elif c == l[1]:
    m[1] = max(m)
    print(min(m))
elif c == l[2]:
    m[2] =max(m)
    print(min(m))