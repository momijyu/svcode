s = str(input())
count = 0
for i in range(len(s)):
    if s[i].islower():
        count += 1
if len(s)/2 < count:
    print(s.lower())
else:
    print(s.upper())