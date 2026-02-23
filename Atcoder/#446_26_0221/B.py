n, m = map(int,input().split())
s = set()
for i in range(n):
    ans= 0
    l = int(input())
    x = list(map(int,input().split()))
    for i in x:
        if i not in s:
            s.add(i)
            ans= i
            break
    print(ans)