s = str(input())
count = 0
m = []
for i in range(len(s)):
    if count == 2:
        l = ",".join(map(str,m))
        m = []
        print(l)
        count = 0
    if s[i] == "#":
        m.append(i+1)
        count += 1
if count == 2:
    l = ",".join(map(str,m))
    m = []
    print(l)
    count = 0