import heapq

lst = [(9,'A'), (8,'B'), (9,'A'), (10,'C'), (15,'A')]
n = int(input())
pq = []

for l in lst:
    heapq.heappush(pq, (l[0], -ord(l[1])))

for i in range(n):
    a = heapq.heappop(pq)
    num = (a[0] * 2) % 17
    var = a[1]
    heapq.heappush(pq, (num, var))

result = []

while pq:
    var1 = heapq.heappop(pq)
    heapq.heappush(result, (var1[0], chr(-var1[1])))
    print(f"({var1[0]}, {chr(-var1[1])}) ", end="")