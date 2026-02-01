n= int(input()) 
count = {}
x = 1
while x * x * 2 < n:
    y = x +1
    while x * x + y * y <= n:
        n = x * x + y * y
        count[n] = count.get(n, 0) +1
        y += 1
    x += 1
good_num = [n for n, count in count.items() if count == 1]
print(len(good_num))
print("".join(good_num))
