from collections import Counter
n, k = map(int,input().split())
a = list(map(int,input().split()))
cnt_a = Counter(a)
print(cnt_a)
if len(cnt_a) < k:
    print(0)
    exit()
cnt_b = []
t = 0
for key, val in cnt_a.items():
    cnt_b.append((key * val, key))
    t += 1
cnt_b.sort()
cnt_b.reverse()
print(cnt_b)
dame = set()
for i in range(k):
    dame.add(cnt_b[i][1])
ans = 0
for i in a:
    if i not in dame:
        ans += i
print(ans) 