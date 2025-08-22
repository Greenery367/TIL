
# 전위 순회

bt = [0, 'A', 'B', 'T', 'R', 'S', 'V']
bt += [0] * 100

def dfs(now): #now는 현재노드
    # 전위순회를 하다가
    # 왼쪽 자식으로 갔는데 0이다. 8번 인덱스에는 노드가 없다.
    # 오른쪽 자식으로 갔는데 9이다. 9번 인덱스에는 노드가 없다.
    # 13이야 잘못 들어갔어 return

    if bt[now] == 0 : return

    print(bt[now])
    dfs(now * 2)
    dfs(now * 2 + 1)

dfs(1)



# 중위 순회

bt = [0, 'A', 'B', 'T', 'R', 'S', 'V']
bt += [0] * 100


def dfs(now):  # now는 현재노드
    # 전위순회를 하다가
    # 왼쪽 자식으로 갔는데 0이다. 8번 인덱스에는 노드가 없다.
    # 오른쪽 자식으로 갔는데 9이다. 9번 인덱스에는 노드가 없다.
    # 13이야 잘못 들어갔어 return

    if bt[now] == 0: return

    dfs(now * 2)
    print(bt[now])
    dfs(now * 2 + 1)

dfs(1)



# 후위 순회

bt = [0, 'A', 'B', 'T', 'R', 'S', 'V']
bt += [0] * 100


def dfs(now):  # now는 현재노드
    # 전위순회를 하다가
    # 왼쪽 자식으로 갔는데 0이다. 8번 인덱스에는 노드가 없다.
    # 오른쪽 자식으로 갔는데 9이다. 9번 인덱스에는 노드가 없다.
    # 13이야 잘못 들어갔어 return

    if bt[now] == 0: return

    dfs(now * 2)
    dfs(now * 2 + 1)
    print(bt[now])


dfs(1)