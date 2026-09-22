n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        s = sum(a[i:j+1])
        check = True
        for z in a[i:j+1]:
            if s % z == 0:
                check = False
        if check :
            cnt += 1
print(cnt)