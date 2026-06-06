s = str(input())
t = str(input())
mi= 'z'
for i in s:
    if i < mi:
        mi = i
for i in t:
    if i > mi:
        print("Yes")
        exit()
print("No")