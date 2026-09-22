s = str(input())
s = list(s)
for i in range(len(s)-1,0,-1):
    if s[i] == "A" and s[i-1] == "W":
        s[i-1] = "A"
        s[i] = "C"
print("".join(s)) 