#https://kenkoooo.com/atcoder/#/contest/show/9438879b-64ce-4495-90d6-7712b009caf2?activeTab=Standings

a, b, c = map(int,input().split())
if a == b:
    print(c)
elif b == c:
    print(a)
elif c == a:
    print(b)
else:
    print(0)