#---------------------------------------------
#フェニック木
class Bit:
    def __init__(self, n, arr):
        self.size = n
        self.tree = [0] * (n + 1)
        for i, val in enumerate(arr):
            self.add(i +1, val)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):# (index,加算したい値)
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
#---------------------------------------------
def solve():
    n, q = map(int,input().split())
    a = list(map(int,input().split()))
    Ftree = Bit(n, a)
    for i in range(q):
        data = list(map(int,input().split()))
        if data[0] == 1:
            x = data[1]
            i1, i2 = x -1, x
            val_1, val_2 = a[i1], a[i2]

            Ftree.add(x, val_2 - val_1)
            Ftree.add(x+1, val_1 - val_2)
            a[i1], a[i2] = a[i2], a[i1]
        else:
            print(Ftree.sum(data[2]) - Ftree.sum(data[1]-1))


if __name__ == "__main__":
    solve()

