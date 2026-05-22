n = int(input())
for i in range(n):
    l = []
    for j in range(n-1):
        a = list(map(int,input().split()))
        l.append(a)
    for a in range(n-2):
        for b in range(n-2-a):
            if l[a][b] + l[a+1][b] < l[a][b+1]:
                print("Yes")
                exit()
    print("No") 
    break