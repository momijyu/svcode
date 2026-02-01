s= str(input())
cnt = 0
for i in range(len(s)):
    if s[i] == "i" or s[i] == "j":
        cnt += 1 
print(cnt)