#セグメント木---------------------------------
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
        print(self.tree) #debug

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

#------------------------------------------

def solve():
    x = [1,1,1,1,1,1]
    segt = SegT_sum(x)
    segt.add(1000, 10)
    print("\nend")
    print(segt.sum(2,10))



if __name__ == "__main__":
    solve()