from collections import Counter
n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
#print(list(c.items()))
ic = list(c.items())
ic.sort(reverse=True)
idx = 0
num = 0
for i in range(len(ic)-1):
    num += ic[i][1]
    print(f"{num}"*(ic[i][0]-ic[i+1][0]), end = "")
num += ic[-1][1]
print(f"{num}"*(ic[-1][0]))

#繰り上がりができてない。
#数字で計算してないから難しいかも
