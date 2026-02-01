n, m = map(int,input().split())
pair = [0]*n
for i in range(m):
    a, b = map(int,input().split())
    pair[a-1] += 1
    pair[b-1] += 1
for i in range(n):
    pp = n-pair[i]-1
    if pp < 3:
        print(0,end = " ")
    else:
        ans = pp *(pp-1) *(pp-2) //6
        print(ans, end = " ")