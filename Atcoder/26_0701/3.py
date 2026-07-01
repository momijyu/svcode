from collections import Counter
n = int(input())
a = list(map(int,input().split()))
ca = Counter(a)
ans = 0
sumn = 0
for v, k in ca.items():
    ans += (n -k -sumn)*k
    sumn += k
print(ans)