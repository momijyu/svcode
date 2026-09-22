def binary_search(l,t):
    start = 0
    end = len(l)-1
    while start <= end:
        mid = (start + end) // 2
        guess = l[mid]
        if guess == t:
            return mid
        if guess > t:
            end = mid -1
        else:
            start = mid +1
    return -1
#-----------------------------------------
def binary_search_near(l,t):
    s = 0
    e = len(l)-1
    while s <= e:
        mid =()
#-----------------------------------------
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
b.sort()
sum = 0
mod = 998244353
for i in range(len(a)):
    print(binary_search(b,a[i]))
    print("aaaaa")
print(sum)