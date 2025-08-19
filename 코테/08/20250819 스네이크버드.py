fruit, snake = map(int, input().split())
fruit_arr = list(map(int, input().split()))

fruit_arr.sort()

for i in fruit_arr :
    if snake >= i:
        snake += 1
    else :
        break

print(snake)