a = list(map(int,input().split()))
s = set()
cnt = 0
for i in range(4):
    for j in range(i+1,4):
        if( a[i] == a[j] ):
            cnt += 1
            print(i,j)
            a[i] = -1
            a[j] = -1
print(cnt) 
print(a)