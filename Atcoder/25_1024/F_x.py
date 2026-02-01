t = int(input())
for i in range(t):
    a, b, c = map(int,input().split())
    N = a + b + c
    print(min(a, c, N // 3))