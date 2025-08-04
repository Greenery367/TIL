# T = int(input())

# for t in range(1, T + 1):
#     width = int(input())
#     arr = list(map(int, input().split()))
    
#     max_drop = 0
    
#     for i in range(width):
#         drop = 0
#         for j in range(i + 1, width):
#             if arr[i] > arr[j]:
#                 drop += 1
#         max_drop = max(max_drop, drop)
    
#     print(f"#{t} {max_drop}")


arr = [2, 5, 1, 6, 4, 3]

total=0
big=0
small=10

for i in arr :
    if small > i :
        small = i
    if big < i :
        big = i
    total += i
    
print(total)
print(big-small)