n = int(input())
w = list(map(str,input().split()))
m ={"and", "not", "that", "the", "you"}
check = True
for i in range(n):
    if w[i] in m:
        check = False
if check:
    print("No")
else:
    print("Yes")