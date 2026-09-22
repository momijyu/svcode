n = int(input())
l = [] 
m = ["0"]
for i in range(n):
    l.append(m)
print(l)
m = l
print(m)
for i in range(n-1):
    l.append(m)
print(l)