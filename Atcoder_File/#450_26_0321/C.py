def dfs(i,j):
    if s[i][j] == ".":
        print(s[i][j])
        S.add((i,j))
        if i != 0 and j != 0 and i != h-1 and j != w-1:
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
    
h, w = map(int,input().split())
s = []
S = set()
for i in range(h):
    a = str(input())
    s.append(a)
print(s[0][0], s)
for i in range(h-1):
    for j in range(1,w-1):
        dfs(i, j)
        

#１、上から下へ探索する、i,j(1,n-1)までで、下と右にお友達がいるかを確認すればいい。
# よく考えたら再帰関数で作れば　いい話じゃないか？