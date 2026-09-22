n = int(input())
for i in range(n):
    l = []
    for j in range(n-1):
        a = list(map(int,input().split()))
        l.append(a)
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if l[a][c-a-1] > l[a][b-a-1] + l[b][c-b-1]:
                    print("Yes")
                    exit()
    print("No") 
    break