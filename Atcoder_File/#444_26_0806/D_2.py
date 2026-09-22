from collections import Counter
n = int(input())
a = list(map(int,input().split()))
c = Counter(a)
#print(list(c.items()))
ic = list(c.items())
ic.sort()
idx = 0
num = len(a)
ans = 0

for i in range()



"""
#print(ic)
for i in range(ic[-1][0]):
    if idx <= len(ic)-1 and i == ic[idx][0]:
        num -= ic[idx][1]
        idx += 1
    ans += (10 ** i)*num 
    #print(111)
print(ans)
"""
#結果変わらないから、考え方違うかも？
#いもす法繰り上がりありとかなら行けるかも？？

"""
for i in range(ic[0][0]):
    now = ic[0][0]-i
    if idx <= len(ic)-1 and now == ic[idx][0]:
        num += ic[idx][1]
        idx += 1
    ans += (10 ** (now-1))* num
    #print(ans)
print(ans)
"""    
#よく考えると10^5(10^5 - 10)くらいなのか、無理。

"""
for i in range(len(ic)-1):
    num += ic[i][1]
    print(f"{num}"*(ic[i][0]-ic[i+1][0]), end = "")
num += ic[-1][1]
print(f"{num}"*(ic[-1][0]))
"""
#繰り上がりができてない。
#数字で計算してないから難しいかも
