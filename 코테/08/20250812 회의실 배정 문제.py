# 회의가 끝나는 시간을 기준으로 정렬
# 만약 종료시간이 같다면 시작 시간이 빠른 순이 우선

# T : 회의의 수
T = int(input())
# meetings : 회의 일정을 tuple로 담은 리스트
meetings = [tuple(map(int, input().split())) for tc in range(T)]

# 회의가 빨리 끝나는 순으로 정렬하기 (람다식 사용)
meetings.sort(key=lambda x: (x[1], x[0]))

# schedule : 스케쥴을 확인하기 위한 배열 생성
schedule =[0 for i in range(1,10)]

# total : 총 회의 개수
total = 0

# meetings의 길이만큼 반복
for j in range(len(meetings)):

    # 만약 회의실의 빈 일정이 없다면 break
    if schedule.count(0) == 0:
        break

    # 만약 해당 회의 일정에 회의실이 비어있다면
    if schedule[meetings[j][0]:meetings[j][1]].count(0) == len(schedule[meetings[j][0]:meetings[j][1]]) :
        # 가능한 회의 개수 추가
        total += 1
        a = meetings[j][0]
        b = meetings[j][1]
        # schedule 배열 값 바꾸기
        for e in range(a, b):
            schedule[e] = 1

# 결과 출력
print(total)