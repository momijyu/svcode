s = str(input())
h = int(len(s)/2)
for i in range(len(s)):
    if i != h:
        print(s[i],end ="")