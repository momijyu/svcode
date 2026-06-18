n = int(input())
w = list(map(int,input().split()))
sw = sum(w)
sw_2 = 0
ans = sw
for i in w:
    sw_2 += i
    diff = abs(sw_2 -(sw - sw_2))
    if diff < ans:
        ans = diff
print(ans)