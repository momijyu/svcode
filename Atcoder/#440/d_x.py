import sys
from bisect import bisect_left, bisect_right

# 入力を高速に受け取る
input = sys.stdin.read
data = input().split()
iterator = iter(data)

n = int(next(iterator))
q = int(next(iterator))

a = []
for _ in range(n):
    a.append(int(next(iterator)))

a.sort()

# 事前計算: 「Ai より小さい数の中に、リストに含まれない数が何個あるか」
# D[i] = (Ai の値) - (Ai が何番目の数か) - 1
# 例: A=[3, 7] -> D=[2, 5]
# 3 は 1,2 が欠けているので 2
# 7 は 1,2,4,5,6 が欠けているので 5
d = []
for i in range(n):
    d.append(a[i] - (i + 1))

ans_list = []

for _ in range(q):
    x = int(next(iterator))
    y = int(next(iterator))

    # 1. X 未満の数字の中に、欠けている数字がいくつあるか？
    # a の中で x より小さいものの個数を数える
    idx_less_x = bisect_left(a, x)
    # (1からx-1までの全個数) - (x未満にあるaの個数)
    missing_before_x = (x - 1) - idx_less_x

    # 2. 全体で何番目の欠損値を探せばいいか？
    target_k = missing_before_x + y

    # 3. リストaの要素を何個飛び越える必要があるか？
    # d 配列の中で target_k - 1 より大きい場所を探す
    idx = bisect_right(d, target_k - 1)

    # 答え = (探したい番目) + (飛び越えたaの個数)
    ans = target_k + idx
    ans_list.append(str(ans))

print('\n'.join(ans_list))
print(d)