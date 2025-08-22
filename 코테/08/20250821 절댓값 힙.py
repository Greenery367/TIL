import sys
import heapq

N = int(input())
arr = []

for n in range(N):
    a = int(sys.stdin.readline().rstrip())

    if a != 0:
        heapq.heappush(arr, (abs(a), a))
    else :
        if not arr: print(0)
        elif arr: print(heapq.heappop(arr)[1])