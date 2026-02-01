from collections import Counter
n, m, c = map(int,input().split())
a = list(map(int,input().split()))
b = Counter(a)
d = list(b.keys())
e = list(b.values())
#print(e,d)
sum = [0] * m
sums = 0
point = 0.5
for i in range(m):
    point = i + 1
    while c > sum[i]:
        if point > max(d):
            point = 0
        if point in d:
            sum[i] += e[d.index(point)]
            sums += e[d.index(point)]
            #print(i,point,d.index(point),e[d.index(point)])
        point += 1
print(sums)