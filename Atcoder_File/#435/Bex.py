n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        s = sum(a[i:j+1])
        check = False
        for z in a[i:j+1]:
            print(i+1,j+1,s,z)
print(cnt)