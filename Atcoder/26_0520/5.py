from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
ans = 0
cnt = 0
hw = []
for k, v in sorted(c.items(), reverse=True):
    if v >= 4:
        hw.append(k)
        hw.append(k)
    elif v >= 2:
        hw.append(k)
    if len(hw) >= 2:
        break
if len(hw) == 2:
    ans = hw[0] * hw[1]
print(ans)