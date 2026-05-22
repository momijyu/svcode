n = int(input())
a = []
b = []
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
m = int(input())
s = []
for i in range(m):
    si = str(input())
    s.append(si)
print(a)
print(b)
print(s)


#新しい配列をつくり、その配列にlen(si) == bi となる配列を入れておいて、並び替えていく？？とか？？言語化難しい、、かも？？
#とりあえず長さaのb文字目を配列に入れればなんとかなる？？わからないけど、、

# p.s. やりたいことはわかるけど、どんな感じに実装すればいいかわからない。