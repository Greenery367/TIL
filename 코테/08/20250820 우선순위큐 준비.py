import heapq

lst = [5,2,8,1,9]
pq = []

for i in lst:
    heapq.heappush(pq, i)

sorted_arr = []

while pq:
    sorted_arr.append(heapq.heappop(pq))
print(sorted_arr)