N, a, b, c = map(int,input().split())
l = [b, c, a]
m = ['F', 'M', 'T']
count = 0
while N > 0:
    N -= l[count % 3]
    count += 1
print(m[count % 3])
print(count)