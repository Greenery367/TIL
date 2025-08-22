import heapq

arr = []
heapq.heappush(arr, 500)
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(arr, a)
    heapq.heappush(arr, b)

    temp = arr.copy()
    sorted_list = []
    while temp:
        sorted_list.append(heapq.heappop(temp))

    print(sorted_list[len(sorted_list)//2])
