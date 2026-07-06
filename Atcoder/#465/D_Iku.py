T = int(input())

for _ in range(T):
  x,y,k = map(int,input().split())
  currX = x
  TX  =[]
  TX.append(x)
  while currX != 0:
    currX //= k
    TX.append(currX)
  print(TX)
  currY = y
  TY = []
  TY.append(y)
  while currY != 0:
    currY //= k
    TY.append(currY)
  print(TY)
  TX.reverse()
  TY.reverse()
  
  length = min(len(TX),len(TY))
  common = 0
  for i in range(length):
    if TX[i] == TY[i]:
      common += 1
    else:
      break
  ans = len(TX)-common +len(TY)-common
  print(ans)
  