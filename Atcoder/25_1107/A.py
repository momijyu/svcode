a, b = map(int ,input().split())
if a % b * 2 > b:
    print(a // b + 1)
else:
    print(a // b)