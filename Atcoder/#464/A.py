s = input()
ls = len(s)
cs = s.count("E")
if cs*2 > ls:
    print("East")
else:
    print("West")