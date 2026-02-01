N, a, b, c = map(int,input().split())
l = [b, c, a]
m = ['F', 'M', 'T']
count = 0
while True:
    if N >= l[count % 3]:
        N -= l[count % 3]
        count += 1
    else:
        print(m[count % 3])
        break