h, w = map(int,input().split())
l = []
for i in range(h):
    row = list(map(str, input().split()))
    l.append(row)
for i in range(1,w-1):
    for j in range(1,h-1):
        if 

#１、上から下へ探索する、i,j(1,n-1)までで、下と右にお友達がいるかを確認すればいい。