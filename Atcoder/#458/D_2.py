# sortされた状態にしながら進める。
# biseceは失敗。heapq嫌いなんだよな...

import heapq
import bisect
x = int(input())
q = int(input())
heap_left = [-x]
heap_right = []
ans = []
idx = 2

for i in range(q):
    a, b = map(int,input().split())
    idx += 2
    median_idx = -heap_left[0]
    for num in [a, b]:
        if num < median_idx:
            heapq.heappush(heap_left, -num)
        else:
            heapq.heappush(heap_right, num)
    #print(heap_left, heap_right)
    tol_len = len(heap_left) + len(heap_right)
    tg = tol_len // 2 + 1
    while len(heap_left) > tg:
        heapq.heappush(heap_right, -heapq.heappop(heap_left))
    while len(heap_left) < tg:
        heapq.heappush(heap_left, -heapq.heappop(heap_right))
    #print(heap_left, heap_right)
    ans.append(-heap_left[0])
print("\n".join(map(str, ans))) 
