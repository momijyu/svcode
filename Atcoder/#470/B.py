from collections import Counter
n = int(input())
c = list(map(int,input().split()))
cc = Counter(c)
#print(cc)
print(len(c)-max(cc.values()))