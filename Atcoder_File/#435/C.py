n = int(input())
a = list(map(int,input().split()))
point = count = 0
for i in range(n):
    count += 1
    if point <= a[i]-1:
        point = a[i]-1
    if point > 0:
        point -= 1
    else:
        break
print(count)