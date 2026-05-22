import heapq
q = int(input())
nums = []
heapq.heapify(nums)
for i in range(q):
    n, h = map(int, input().split())
    if n == 1:
        heapq.heappush(nums, h)
    else:        
        while nums and nums[0] <= h:
            heapq.heappop(nums)
    print(len(nums))
