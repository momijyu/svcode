n, a, b = map(int,input().split())
s = str(input())
count = 0
for i in range(n-1):
    l = []
    for j in range(i,n):
        l += s[j]
        if l.count("b") > b:
            break
        elif l.count("a") >= a:
            count += 1
print(count)