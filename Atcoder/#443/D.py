t = int(input())
for i in range(t):
    n = int(input())
    r = list(map(int,input().split()))
    sum_num = sum(r)
    for i in range(n -1):
        if r[i+1] > r[i]+1:
            r[i+1] = r[i]+1
    for i in range(n -1, 0, -1):
        if r[i-1] > r[i] +1:
            r[i-1] = r[i] +1
    print(sum_num - sum(r))

#a[i] と a[i+1]の差を1にしたいってこと？っぽい？
#なんか値ズレる、、、l7,l8 r[i+1]か