n, m =map(int,input().split())
s = input()
t = input()
cnt = [0]* (len(s)-len(t)+1)
for i in range(n-m+1):
    for j in range(m):
        cnt[i] += (int(s[i+j])-int(t[j]))%10
print(min(cnt))