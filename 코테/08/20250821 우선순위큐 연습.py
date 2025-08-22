import heapq

arr = [5, 2, 8, 1, 9]

pq = []

for x in arr :
    heapq.heappush(pq,x)

sorted_arr = []
while pq:
    sorted_arr.append(heapq.heappop(pq))

print(pq)