from collections import deque

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    cheese = list(map(int, input().split()))
    # 인덱스 1부터 시작, 치즈양
    # enumerate 중요!!!
    pizzas = deque([[i+1, p] for i, p in enumerate(cheese)])

    oven = deque()
    for _ in range(N):
        if pizzas : oven.append(pizzas.popleft())

    # 화덕에 피자가 하나 남을 때까지 반복
    while len(oven) > 1 :
        now = oven.popleft() # 화덕에서 피자 하나 꺼냄]
        # now = [피자 인덱스, 치즈의 양]
        now[1] //= 2
        if now[1] == 0 :
            if pizzas :
                oven.append(pizzas.popleft())
        else :
            oven.append(now)

    # while 문 종료시 피자 하나만 남아있다
    # 피자의 번호 출력
    # [피자 인덱스, 치즈의 양
    print(f"#{tc} {oven[0][0]}")