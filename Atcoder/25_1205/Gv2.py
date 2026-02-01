from bisect import bisect_left, bisect_right
from itertools import accumulate
n = int(input())
x = list(map(int, input().split()))
p = list(map(int,input().split()))
q = int(input())
pac = [0]+list(accumulate(p))
for i in range(q):
    sum = 0
    l, r = map(int,input().split())
    for j in range(l, r+1):
        idxl = bisect_left(x, l)
        idxr = bisect_right(x, r)
        sum = pac[idxr] - pac[idxl]
    print(sum)