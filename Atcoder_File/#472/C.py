n, m, k = map(int,input().split())
a = list(map(int,input().split()))
nowk= 0
eat = [False]*n
for i in range(n):
    if nowk + a[i] <= k:
        nowk += a[i]
        eat[i] = True
        print("Yes")
    else:
        print("No")
    #print(nowk)
    #print(eat)
    if i >= (m-1) and eat[i-(m-1)] == True:
        nowk -= a[i-(m-1)]
