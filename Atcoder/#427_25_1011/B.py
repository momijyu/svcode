N = int(input())
l = [0] * (N + 1)
l[0] = 1
sum = 0
for i in range(1, N + 1):
    x = str(l[i-1])
    for j in range (len(x)):
        sum += int(x[j])
    l[i] = sum
print(l[-1])