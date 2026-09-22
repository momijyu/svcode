t = int(input())
for i in range(t):
    n, d = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    id = 0
    loss = -1
    for j in range(n):
        loss = j - d
        a[id] -= b[j]
        for z in range(id, j):
            if a[z] < 0:
                a[z+1] += a[z]
                a[z] = 0
        if loss > -1:
            a[loss] = 0
    print(sum(a))

"""
最初は何もない、
追加する
使う
賞味期限を見て捨てる

考え方1：与えられたarrをそのまま最初から使い捨てながら減らしていく。❌
考え方2：その時点で使った卵、仕入れた卵の合計から捨てる数を算出する方法。
"""