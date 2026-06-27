n = int(input())
ai = []
bi = []
for i in range(n):
    a, b = map(int,input().split())
    ai.append((a, i))
    bi.append((b, i))
#print(ab)
ai.sort()
bi.sort()
#print(ai, bi)
if ai[0][1] != bi[0][1]:
    print(max(ai[0][0],bi[0][0]))
else:
    print(min(ai[0][0]+bi[0][0], max(ai[1][0], bi[0][0]), max(ai[0][0], bi[1][0])))