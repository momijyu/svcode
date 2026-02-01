n = int(input())
s = input()
a = s.count("A")
t = s.count("T")
if a < t:
    print("T")
elif a > t:
    print("A")
else:
    if s[-1] == "T":
        print("T")
    else:
        print("A")