s = str(input())
hf = len(s) //2
lens = len(s)
cnt = 0
for i in range(len(s)):
    if s[i] == "C":
        cnt += min(i + 1, lens -i)
print(cnt)