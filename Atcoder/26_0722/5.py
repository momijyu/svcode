from collections import Counter
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
#print(a)
ca = Counter(a)
ca = sorted(ca.items())
ca.reverse()
#print(ca)
ans = 1
cnt = 0
for i in range(len(ca)):
    if ca[i][1] > 3 and cnt == 0:
        print(ca[i][0]*ca[i][0])
        exit()
    if ca[i][1] > 1:
        ans *= ca[i][0]
        cnt += 1
    if cnt == 2:
        break
if cnt == 0:
    print(0)
    exit()
print(ans)