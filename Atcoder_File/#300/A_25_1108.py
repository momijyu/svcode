n, a, b= map(int,input().split())
c = list(map(int,input().split()))
count= 1
for i in c:
    if i == a + b:
        print(count)
        break
    count += 1