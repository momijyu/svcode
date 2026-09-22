a, b = map(int,input().split())
#print(a/4,b/4)
if a+1 == b:
    if (a-0.1)//3 == (b-0.1)//3:
        print("Yes")
    else:
        print("No")
else:
    print("No")