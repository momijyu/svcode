N = int(input()) 
S = str(input())
count = 0
for i in range(N-2):
    if S[i] == "#":
         if S[i+1] == ".":
              if S[i+2] == "#":
                   count += 1
print(count)