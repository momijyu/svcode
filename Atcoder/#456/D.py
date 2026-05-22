s = str(input())
a = [0] * 5
# a, ba, ca, bca, cba, aで終わる組み合わせ
b = [0] * 5
# b, ab, cb, acb, cab
c = [0] * 5
# c, ac, bc, abc, bac
for i in s:
    if i == "a":
        a[0] += 1
        a[1] += b[0]
        a[2] += c[0]
        a[3] += c[2]
        a[4] += b[2]
        continue
    if i == "b":
        b[0] += 1
        b[1] += a[0]
        b[2] += c[0]
        b[3] += c[1]
        b[4] += a[2]
        continue
    if i == "c":
        c[0] += 1
        c[1] += a[0]
        c[2] += b[0]
        c[3] += b[1]
        c[4] += a[1]
        continue
print((sum(a) + sum(b) + sum(c))% 998244353)
print(a, b, c)