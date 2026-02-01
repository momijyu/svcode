x, y = map(str, input().split())
l = ["Ocelot", "Serval", "Lynx"]

if l.index(x) >= l.index(y):
    print("Yes")
else:
    print("No")