from collections import Counter
n = int(input())
a = list(map(int,input().split()))
b = Counter(a)
c = list(b.values())
count = 0
for i in range(len(c)):
    count += c[i] * (c[i]-1) //2 * (n -c[i])
print(count)