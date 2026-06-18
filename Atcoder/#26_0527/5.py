col = [True]*9
n = int(input())
a = list(map(int,input().split()))
cnt = 0
cnt_2 = 0
for i in range(n):
    if a[i] < 400 :
        if col[0]:
            col[0] = False
            cnt +=1
    elif a[i] < 800 :
        if col[1]:
            col[1] = False
            cnt += 1
    elif a[i] < 1200 :
        if col[2]:
            col[2] = False
            cnt += 1
    elif a[i] < 1600 :
        if col[3]:
            col[3] = False
            cnt += 1
    elif a[i] < 2000 :
        if col[4]:
            col[4] = False
            cnt += 1
    elif a[i] < 2400 :
        if col[5]:
            col[5] = False
            cnt += 1
    elif a[i] < 2800 :
        if col[6]:
            col[6] = False
            cnt += 1
    elif a[i] < 3200 :
        if col[7]:
            col[7] = False
            cnt += 1
    else:
       cnt_2 += 1
if cnt_2 > 0:
    print(max(cnt,1), cnt+cnt_2)
else:
    print(max(cnt,1), cnt)