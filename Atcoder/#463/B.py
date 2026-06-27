n, x = input().split()
y = 0
s = []
n = int(n) 
cnt = 0
if x == "A":y= 0
if x == "B":y= 1
if x == "C":y= 2
if x == "D":y= 3
if x == "E":y= 4

for i in range(n):
    sa = input()
    s.append(sa)
for i in range(n):
    if s[i][y] == 'o':
        print("Yes")
        exit()
print("No")
#print(y)