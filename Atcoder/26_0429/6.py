n = int(input())
s = str(input())
ans = []
k = 0
for i in s:
    if i == '(':
        k += 1
    elif i == ')':
        if k > 0:
            k -= 1
    else:
        if k == 0:
            ans.append(i)
print("".join(ans))