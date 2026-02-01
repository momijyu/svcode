class SegT_sum:
    def __init__(self, arr):
        n = len(arr)
        tmp, inf = 1, 0
        while tmp < n:tmp *= 2
        self.size = tmp
        self.tree = [0] * (self.size * 2)
        for i in range(1,n+1):
            self.add(i,arr[i-1])
    
    def add(self, idx, val):
        if self.size < idx:return
        i = self.size + idx -1 
        while i > 0:
            self.tree[i] += val
            i //= 2
        #print(self.tree) #debug

    def sum(self, start, end):
        if self.size < end:return -1
        sum = 0
        start += self.size-1
        end += self.size-1
        while start <= end:
            if start % 2 == 1:
                sum += self.tree[start]
                start += 1
            if end % 2 == 0:
                sum += self.tree[end]
                end -= 1
            start //= 2
            end //= 2
        return sum 


def solve():
    n, q = map(int,input().split())
    a = list(map(int,input().split()))
    segt = SegT_sum(a)
    #print()
    for i in range(q):
        data = list(map(int,input().split()))
        if data[0] == 1:
            idx_1 = data[1]
            idx_2 = data[1]+1
            val_1 = a[idx_1-1]
            val_2 = a[idx_2-1]
            segt.add(idx_1,val_2 - val_1)
            segt.add(idx_2,val_1 - val_2)
            a[data[1]-1], a[data[1]] = a[data[1]],a[data[1]-1]
        else:
            print(segt.sum(data[1],data[2]))
            

if __name__ == "__main__":
    solve()