# 1. 최소힙 2. 최대힙 3. 다중조건힙

# 1. 최소힙
import heapq

pq = []
heapq.heappush(pq, 3)
heapq.heappush(pq, 1)
heapq.heappush(pq, 4)

while pq:
    print(heapq.heappop(pq))


# 2. 최대힙
pq = []
heapq.heappush(pq,-3)
heapq.heappush(pq,-1)
heapq.heappush(pq,-4)

# 뺄 때는 다시 -를 붙여서 양수로 전환
while pq:
    print(-heapq.heappop(pq))


# 3. 다중조건 힙
pq = []
heapq.heappush(pq,(2,'A')) # 우선 순위 -> 1. 정수, 2. 문자열
heapq.heappush(pq,(2,'B'))
heapq.heappush(pq,(4,'C'))

while pq:
    print(heapq.heappop(pq))