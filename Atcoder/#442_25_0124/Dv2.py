class Bit:
    def __init__(self, n, arr):
        self.size = n
        self.tree = [0] * (n + 1)
        for i, val in enumerate(arr):
            self.add(i + 1,val)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def solve():
    n, q = map(int,input().split())
    a = list(map(int,input().split()))
    Ftree = Bit(n, a)
    for i in range(q):
        x = list(map(int,input().split()))
        if x[0] == 1:
            idx_1 = x[1]-1
            idx_2 = x[1]
            val_1 = a[idx_1]
            val_2 = a[idx_2]
            Ftree.add(idx_1, val_2 -val_1)
            Ftree.add(idx_2, val_1 -val_2)
            a[idx_1], a[idx_2] = a[idx_2], a[idx_1]
        else:
            print(Ftree.sum(x[2])-Ftree.sum(x[1]-1))

if __name__ == "__main__":
    solve()