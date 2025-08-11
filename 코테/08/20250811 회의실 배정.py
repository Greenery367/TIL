# 1. 입력 받기
n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

# 2. 정렬하기
# TODO: 위에서 설명한 정렬 기준에 따라 meetings 리스트를 정렬하세요.
meetings.sort(key=lambda x: (x[1], x[0]))

# 3. 회의 선택하기
count = 0
last_end_time = 0

# TODO: 정렬된 meetings 리스트를 순회하며 회의를 선택하는 로직을 작성하세요.
#       hint: 'last_end_time' 변수와 'count' 변수를 활용합니다.

print(count)