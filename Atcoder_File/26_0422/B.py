import math 
n = int(input())
x = list(map(int,input().split()))
ans_1 = 0
ans_2 = 0
ans_3 = []
for i in range(n):
    ans_3.append(abs(x[i]))
    ans_1 += ans_3[i]
    ans_2 += ans_3[i] ** 2
print(ans_1, math.sqrt(ans_2), max(ans_3), sep="\n")