n = int(input())
a = list(map(int,input().split()))
set1 = set()
count = 0
for i in range(n):
    for j in range(i+1,n):
        if a[j] not in set1:
            set1.add(a[j])
            count += a.count(a[j])*(a.count(a[j])-1)/2
        print(i,j,count,set1, a.count(a[j]),end="")
        print(a)
    a[i] = 0
    set1.clear()




        