n, q = map(int,input().split())
arr = [0]*n
for i in range(q):
    a = list(map(int,input().split()))
    if a[0] == 1:
        arr[a[1]-1]+= 1
    else:
        for i in range(n):
            if arr[i] != 0:
                arr[i]-= 1
    sums = 0
    for i in range(n-1):
        sums += arr[i]^arr[i+1]
    print(sums)