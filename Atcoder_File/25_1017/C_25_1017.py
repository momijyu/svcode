S = str(input())
T = str(input())
count = 0
count2 = 0
check = 0
for i in range(len(S)):
    if S[i].isupper() and count == 1:
        if S[i-1] in T:
            check +=1
        count2 += 1
    elif S[i].isupper():
        count += 1
if S.islower():
    check = count2
if check != count2:
    print("No")
else:
    print("Yes")
