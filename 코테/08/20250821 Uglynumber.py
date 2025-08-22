import heapq

Q = int(input())
arr = list(map(int, input().split()))
max_k = max(arr)

# 최소 힙, 방문 기록
pq = [1]
visited = set([1])
ugly = []

while len(ugly) < max_k:
    x = heapq.heappop(pq)
    ugly.append(x)

    for factor in [2, 3, 5]:
        next_ugly = x * factor
        if next_ugly not in visited:
            heapq.heappush(pq, next_ugly)
            visited.add(next_ugly)

# 출력
for k in arr:
    print(ugly[k - 1], end=' ')
