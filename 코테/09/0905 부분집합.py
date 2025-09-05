T = int(input())

def dfs(idx, cnt, total):
    global answer
    if cnt > N or total > K:
        return
    if idx == 12:
        if cnt == N and total == K:
            answer += 1
        return

    dfs(idx+1, cnt+1,total+nums[idx])
    dfs(idx+1, cnt,total)

for tc in range(1, T+1):
    N,K = map(int, input().split())
    nums = list(range(1,13))
    answer = 0

    dfs(0,0,0)
    print(f"#{tc} {answer}")