n, a, b = input().split()
s = str(input())
l = list(s)
for i in range(len(s)):
    if s[i] != a:
        l[i] = b       
print("".join(l))