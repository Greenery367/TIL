cards = list(map(int, input().split()))

found = False  # baby-gin 여부

def is_valid(group):
    group.sort()
    return (group[0] == group[1] == group[2]) or (group[0]+1 == group[1] and group[1]+1 == group[2])

def pick_comb(i, picked, used):
    global found
    if found:
        return  # 이미 찾았으면 종료

    if len(picked) == 3:
        # 앞의 3개 picked, 나머지 3개 만들기
        rest = []
        for j in range(6):
            if not used[j]:
                rest.append(cards[j])

        if is_valid(picked[:]) and is_valid(rest[:]):
            found = True
        return

    if i >= 6:
        return

    # 이 카드 선택
    used[i] = True
    picked.append(cards[i])
    pick_comb(i+1, picked, used)
    picked.pop()
    used[i] = False

    # 이 카드 선택 안 함
    pick_comb(i+1, picked, used)

used = [False] * 6
pick_comb(0, [], used)

print("Yes" if found else "No")
