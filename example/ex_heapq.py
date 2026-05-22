import heapq
numbers = []
heapq.heapify(numbers)
heapq.heappush(numbers, 5)
heapq.heappush(numbers, 2)
print(heapq.nsmallest(2, numbers))
print(heapq.nlargest(3, numbers))
print(numbers)

#作ったheapqは、最小値を優先するヒープ構造であるため、
#最小値を取得するのに適しています。最大値を取得するには、
#heapq.nlargest()関数を使用することができます。

#heapq.nsmallest() は min
#heapq.nlargest() は max
#heapq.heappop() は最小値を取り出す
#heapq.heappush() は値を追加する
#heapq.heapify() はリストをヒープ構造に変換する
