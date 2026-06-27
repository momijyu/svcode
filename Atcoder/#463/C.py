class SegT_max:
    def __init__(self,arr):
        n = len(arr)
        #配列を2累乗にしたい
        tmp = 1
        while tmp < n:tmp *= 2
        self.size = tmp
        self.tree = [0] * self.size * 2
        for i in range(1,n+1):
            self.add(i,arr[i-1])

    def add(self, idx, val):
        if self.size < idx:return
        i = self.size + idx -1 
        self.tree[i] += val
        while i > 0:
            if i % 2 == 0:
                self.tree[i//2] = max(self.tree[i],self.tree[i+1])
            else:
                self.tree[i//2] = max(self.tree[i],self.tree[i-1])
            i //= 2
    def update(self, idx, val):
        i = self.size + idx
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = max(self.tree[i*2], self.tree[i*2+1])
#-----------------------------------------------------

n = int(input())
lin = []
h = []
for i in range(n):
    hi, li = map(int,input().split())
    h.append(hi)
    lin.append((li,hi))
#print(h, l )
lin.sort(reverse=True)
ht = SegT_max([0] * n)
pidx = 0
q = int(input())
t = list(map(int,input().split()))
qu = []
for i in range(q):
    qu.append((t[i],i))
qu.sort(reverse=True)
ans = [0] * q
for t, qidx in qu:
    while pidx < n and lin[pidx][0] > t:
        ht.update(pidx, lin[pidx][1])
        pidx += 1
    ans[qidx] = ht.tree[1]
for a in ans:
    print(a)