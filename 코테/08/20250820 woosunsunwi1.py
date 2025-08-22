import heapq

lst = [5,2,8,1,9,4]

pq = []

for i in lst :
    first = 0
    if i % 2 == 0 : first = 0
    else : first = 1
    heapq.heappush(pq,(first, i))

result = []

while pq:
    result.append(heapq.heappop(pq)[1])

print(*result)