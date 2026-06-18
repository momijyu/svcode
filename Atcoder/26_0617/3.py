from collections import Counter

n = int(input())
x = []
for i in range(n):
    xa, ya = map(int,input().split())
    x.append((xa, ya))
"""
cx = Counter(x)
cy = Counter(y)
mx = list(cx.values())
my = list(cy.values())
print(mx, my)
if mx[0] > 2 or my[0] > 2:
    print("Yes")
else:
    print("No") 
"""
print(x)
