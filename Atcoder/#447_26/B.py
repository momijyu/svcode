s = str(input())
se = set()
l= []
for i in range(len(s)):
    if s[i] not in se:
        l.append((s[i], s.count(s[i])))
        se.add(s[i])
print(max(l))