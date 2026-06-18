a, b, c = map(int,input().split())
for i in range(a*b):
    ss = ""
    for j in range(a*c):
        if (i//b + j//c) % 2 == 0:
            ss += '.'
        else:
            ss += '#'
    print(ss)