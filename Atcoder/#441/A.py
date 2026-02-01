p, q= map(int,input().split())
x, y= map(int,input().split())
if(p <= x and q <= y and p+99 >= x and q+99 >= y):
    print("Yes")
else:
    print("No")