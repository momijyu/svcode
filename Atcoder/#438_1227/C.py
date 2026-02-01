n = int(input())
a = list(map(int,input().split()))
b = [(a[0],1)]
for i in range(1,n):
    if len(b) != 0 and b[-1][0] == a[i]:
        val, cnt = b.pop()
        new_cnt = cnt + 1
        if new_cnt < 4:
            b.append((val, new_cnt))
    else:
        b.append((a[i],1))
print(sum(cnt for val, cnt in b))