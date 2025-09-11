path = []

def dfs(idx):
    if idx > 10:
        if sum(path) < 11:
            print(*path)
        return

    # ① 현재 숫자 포함
    path.append(idx)
    dfs(idx + 1)
    print(f"1111{path}")

    # ② 현재 숫자 미포함 (백트래킹)
    path.pop()
    dfs(idx + 1)
    print(f"2222{path}")

dfs(1)
