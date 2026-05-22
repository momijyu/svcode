q = int(input())
s = []
ms = 10 ** 10
for i in range(q):
    n, h = map(int, input().split())
    if n == 1:
        s.append(h)
        ms = min(s)
    elif h >= ms:
        s.sort()
        s.reverse()
        while h >= ms:
            s.pop()
            ms = min(s)
    print(len(s))
    print(s)