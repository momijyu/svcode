s, a, b, x = map(int,input().split())
time = a + b
m = int(x /time)
m2 = x % time
#print(m2, m)
sum = m * s * a
if m2 > 0:
    if m2 <= a:
        sum += m2 * s
    if m2 > a:
        sum += a * s
        m2 -= a
print(sum)