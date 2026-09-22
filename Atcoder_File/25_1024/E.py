n, m = map(int,input().split())
s = list(str(input()))
c = list(input().split())
buf1 = "o"
buf2 = "i"
check = True
count = 0
for i in range(m):
    for j in range(n):
        if c[j] == str(i+1) and count %2 == 0:
            s[j] = buf1
            buf2 = s[j]
            count += 1
        elif c[j] == str(i+1):
            s[j] = buf2
            buf1 = s[j]
            count += 1
        if check:
            check = False
            a = j
    if count %2 == 0:
        s[a] = buf1
    else:
        s[a] = buf2
    count = 0
print(s)