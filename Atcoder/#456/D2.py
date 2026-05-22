s = input()
m = 998244353

a = 0
b = 0
c = 0
#その文字で終わる数
for i in s:
    if i == "a":
        a += 1
        a += b
        a += c
        #print("a",a)
    elif i == "b":
        b += 1
        b += a
        b += c
        #print("b", b)
    elif i == "c":
        c += 1
        c += a
        c += b
        #print("c", c)

print((a + b + c) % m)