import heapq

lst = [('BHC', 2), ("NeNe", 1), ("KFC", 3), ("BBQ", 1), ("Moms", 2), ("Mc", 4)]
pq = []

# 초기 heap 구성 (우선순위, 이름) 튜플 -> 이름순 자동 정렬됨
for item in lst:
    heapq.heappush(pq, (item[1], item[0]))

# 반복적으로 합치기
while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)

    # 이름은 사전순으로 더 작은 쪽 사용 (그게 heap 조건 유지에 도움)
    new_name = min(a[1], b[1])
    new_priority = a[0] + b[0]

    heapq.heappush(pq, (new_priority, new_name))

# 최종 결과 출력
print(pq[0])  # → (total_weight, "BBQ") 형태로 출력되기를 기대
