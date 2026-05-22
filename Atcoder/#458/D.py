#sortされた状態にしながら進める。
import heapq
import bisect
x = int(input())
q = int(input())
blackb = [x]
ans = []
for i in range(q):
    a, b = map(int,input().split())
    bisect.insort(blackb, b)
    bisect.insort(blackb, a)
    ans.append(blackb[len(blackb)//2])
print("\n".join(map(str, ans)))