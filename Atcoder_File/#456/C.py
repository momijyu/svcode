s = str(input())
ns = s[0]
#今の値をk録
cnt_s = 1
#繋がりの確認
ans = 0
for i in range(1,len(s)):
    if ns != s[i]:
        cnt_s += 1
    else:
        ans += sum(range(cnt_s+1))
        cnt_s = 1
    ns = s[i]
ans += sum(range(cnt_s+1))
print(ans % 998244353)