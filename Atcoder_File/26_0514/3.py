n = int(input())
p = list(map(int,input().split()))
i = n
cnt= 0
while i != 1:
    cnt += 1
    i = p[i-2]
print(cnt)