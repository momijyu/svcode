h, w = map(int,input().split())
s = "snuke"
l = []
for i in range(h):
    l.append(input())
for i in range(h):
    if s[0] in l[i]:
        p = l[i].index(s[0])
        if s in l[i]:
            for j in range(p, w):
                print(i+1, j+1)
            if i <= w:
                if l[i-1] == s[1] and l[i-2] == s[2] and l[i-3] == s[3] and l[i-4] == s[4]:
                    print(p,i+1)
                    print(p,i)
                    print(p,i-1)
                    print(p,i-2)
                    print(p,i-3)