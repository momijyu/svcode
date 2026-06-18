s = input()
s_ = sorted(s)
t = input()
t_ = sorted(t)
t_.reverse()
if s_ < t_:
    print("Yes")
else:
    print("No")