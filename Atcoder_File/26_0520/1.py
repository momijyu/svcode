# https://kenkoooo.com/atcoder/#/contest/show/b9088dec-b6fd-4df6-8cfc-294840661a92?activeTab=Probleme
a, b = map(int, input().split())
if abs(a - b) < 3:
    print("Yes")
else:
    print("No")