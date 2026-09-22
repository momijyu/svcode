N = int(input())
S = [] 
for i in range(N):
    a = input()
    S.append(a)
for i in range(N):
    for j in range(N):
        if(i != j):
            l1 = list(S[i] + S[j])
            l2 = l1[:]
            l2.reverse()
            if l1 == l2:
                print("Yes")
                exit()
print("No")