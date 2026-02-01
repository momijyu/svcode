s = []
S = str(input())
for i in S:
    s.append(i)
    if len(s) > 3 and s in ("abc"):
        print(100)