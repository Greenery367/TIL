import heapq

N = int(input())

lst = []
heapq.heappush(lst, 500)

for n in range(N):
    a,b = map(int, input().split())
    heapq.heappush(lst, a)
    heapq.heappush(lst, b)
    lst.sort()

    print(lst[len(lst)//2])