from collections import Counter
a = []
cnt_a = []
cnt = []
ans = []
for i in range(3):
    ar = list (map(int,input().split()) )
    for ii in range(4,7):
        cnt_ar = ar.count(ii) /6
        cnt_a.append(cnt_ar)
    cnt.append(cnt_a)
    cnt_a = []
for i in range(3):
    for ii in range(3):
        for iii in range(3):
            if i != ii and ii != iii and i != iii:
                ans.append(cnt[0][i] * cnt[1][ii] * cnt[2][iii])
print(sum(ans ))