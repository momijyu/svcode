from collections import Counter
n = int(input())
a = list(map(int,input().split()))
ac = Counter(a)
q = int(input())
ans  = 0
for k, v in ac.items():
    ans += k * v
for i in range(q):
    b, c = map(int,input().split())
    ans += (c -b)*ac[b] 
    ac[c] += ac[b]
    ac[b] = 0
    print(ans)