n, m, t = map(int,input().split())
a = list(map(int, input().split()))
X = [0]* (m+1)
Y = [0]* (m+1)
n -= 1
chack = True
for i in range(m):
    X[i],Y[i] = map(int,input().split())
print(X, Y)
num = 0
count = 0
while num < n:
    if t >= a[num]:
        t -= a[num]
        num += 1
    else:
        chack = False
        print("No")
        break
    if num == X[count]-1:
        print(t)
        t += Y[count]
        count += 1
if chack:
    print("Yes")