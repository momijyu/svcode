def kitaiti(a):
    #print((a+1)/2, (b+1)/2, (c+1)/2)
    return (sum(a)+len(a))/2

n, k = map(int,input().split())
p = list(map(int,input().split()))
max_idx = k-1
max_sum = sum(p[:k])
now_sum = max_sum
for i in range(k,n):
    now_sum += p[i]-p[i -k]
    if now_sum > max_sum:
        max_sum = now_sum
        max_idx = i
print(kitaiti(p[max_idx-k +1:max_idx + 1]))
#print(p[max_idx-2],p[max_idx-1],p[max_idx])
#print(max_idx)