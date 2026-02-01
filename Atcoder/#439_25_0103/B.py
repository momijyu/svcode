n = int(input())
s= set()
while n != 1 and n not in s:
    s.add(n)
    n = sum(int(digit)**2 for  digit in str(n))
if n == 1:
    print("Yes")
else:
    print("No")