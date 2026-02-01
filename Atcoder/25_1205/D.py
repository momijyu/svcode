n = int(input())
log = False
er = 0
for i in range(n):
    s = str(input())
    if s == "login":
        log = True
    if s == "logout":
        log = False
    if s == "private":
        if log != True:
            er += 1
print(er)