n = int(input())
s = str(input())
j = 0
for i in range(n):
    if j <= n-1:
        while j < n and s[j] == "o":
            j += 1
        if j <= n-1:
            j += 1
    print(j)
    