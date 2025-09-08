# [문제] 동전의 최소 개수
# 규칙: 큰 동전부터 나누지
coin = [50,100,500,10]
target = 1730
cnt = 0
result = 0

# Greedy 문제의 단골 손님 : sort (정렬)
# 정렬 연습  튜플이라면? 인스턴스 리스트? 역순이라면?
# 길이가 우선 정렬, 같은 길이는 사전 순으로 정렬
# list.sort() vs list.sorted() 차이점
coin.sort(reverse = True) # 큰 동전 순으로 정렬

for c in coin:
    # 현재 동전으로 가능한 최대 수
    possible_cnt = target // c
    result += possible_cnt

    # 정답에 더해준다
    target -= c * possible_cnt

    # 금액을 빼준다
    print(result)