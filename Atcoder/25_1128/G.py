s = str(input())
k = int(input())
c = []
count = 0
for i in range(len(s)):
    if s[i] == ".":
        c.append(count)
        count = 0
    else:
         count += 1
c.append(count)
for i in range(len(s)):