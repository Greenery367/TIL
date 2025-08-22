import heapq

lst = [(7,'A'),(9,'C'),(7,'C'),(6,'D'),(5,'A')]
pq = []

for i in lst :
    first = ord(i[1])
    heapq.heappush(pq, (first, -(int(i[0]))))

result = []

while pq:
    a = heapq.heappop(pq)
    aa = chr(a[0])
    bb = -a[1]
    result.append((bb,aa))
    if len(pq) == 0: print(f"({bb}, {aa})", end="")
    else : print(f"({bb}, {aa})", end=" ")

