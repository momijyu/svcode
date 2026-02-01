T = int(input())
count = 0
for i in range(T):
    n = int(input())
    l = list(map(int,input().split()))
    for i in range(len(l)):
        if l[i] % 2 != 0:
            count += 1
    print(count)
    count = 0