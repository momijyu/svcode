n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max_a = max(a)
print(sum(a) - max_a//2)