from sortedcontainers import SortedList
x= int(input())
q= int(input())

ans= SortedList([x])
n= 1
for i in range(q):
    a,b= map(int,input().split())
    n += 2
    ans.add(a)
    ans.add(b)
    print(ans[n//2])