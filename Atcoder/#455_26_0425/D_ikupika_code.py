N,Q = map(int,input().split())
C = []
P = []
for i in range(Q):
  c,p = map(int,input().split())
  C.append(c)
  P.append(p)
  
T = {}

for i in range(N):
  T[i+1] =[]
c = [False for _ in range(N)]
  
for i in range(Q-1,-1,-1):
  if not(c[C[i]-1]):
    T[P[i]].append(C[i])
    c[C[i]-1] = True

for i in range(N):
  ans = 0
  idx = i+1
  if not(c[i]):
    ans += 1
    while T[idx]:
      ans += 1
      idx = T[idx][0]
  print(ans,end = ' ')      
print(c)
print(T)