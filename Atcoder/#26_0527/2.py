x = input()
if '.' in x:
    ans = x.split('.')[0]
else:
    ans = x
print(ans)