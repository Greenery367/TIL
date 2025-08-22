import heapq

pq = []

heapq.heappush(pq,5)
heapq.heappush(pq,2)
heapq.heappush(pq,8)
heapq.heappush(pq,1)
heapq.heappush(pq,9)
print(pq) -> 1,2,8,5,9

sorted_arr = []

while pq:
    sorted_arr.append(heapq.heappop(pq))

print(sorted_arr)