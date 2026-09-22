n, m = map(int,input().split())
a = list(input().split())
#print(a)
print(n-m, end= "\n")
for i in range(n):
    if str(i+1) not in a:
        print(i+1,end=" ")