l, a= map(int,input().split())
if l % a == 0:
    print(l // a)
else:
    print(l // a + 1)
