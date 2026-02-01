n, k = map(int,input().split())
import collections
s = str(input())
msgs = []
for i in range(n-k+1):
    msg = s[i] + s[i+1] + s[i+2]
    msgs.append(msg)
m = collections.Counter(msgs)
print(m)
print(m.keys(max(m.values())))
print(max(m.values()))
print(msgs)