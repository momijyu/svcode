def min2rl(b_l, b_r):
    ans = 0
    r_idx = len(b_r) - 1
    for l_idx in range(len(b_l)):
        cost_l = b_l[l_idx] * 2 
        if cost_l > l:
            break
        while cost_l + b_r[r_idx] > l:
            r_idx -= 1
        ans = max(ans, l_idx + r_idx + 1)
    return ans

n, s, l = map(int,input().split())
a = list(map(int,input().split()))
a_l = a[0:s-1][::-1]
a_r = a[s-1:]
#print(a_l, a_r)
b_l = [0]* (len(a_l)+1)
b_r = [0]* (len(a_r)+1)
for i in range(len(a_l)):
    b_l[i + 1] = b_l[i] + a_l[i]
for j in range(len(a_r)):
    b_r[j + 1] = b_r[j] + a_r[j]

ansx = min2rl(b_l, b_r)
ansy = min2rl(b_r, b_l)
print(max(ansx, ansy))