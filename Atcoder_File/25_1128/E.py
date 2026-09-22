n = int(input())
b = []
h = []
sum = 0
for i in range(n):
    a, d = map(int,input().split()) 
    sum += a
    b.append(d)
    h.append(d-a)
print(sum+max(h))