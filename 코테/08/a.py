# 테스트 케이스의 수
T = int(input())

for i in range(T):
    # n : 총 학생 수
    # k : 학점을 알고 싶은 학생의 번호
    n, k = map(int, input().split())

    # 점수 리스트
    score_arr = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 
             'C+', 'C0', 'C-', 'D0']

    # 모든 학생들의 점수 리스트
    std_arr = []

    # 점수 비율에 맞게 계산 후 리스트 추가
    for j in range(n) :
        mid, fin, hom = map(int, input().split())
        std_arr.append(round(mid*0.35 + fin*0.45 + hom*0.2))

    # 물어본 학생의 값
    ask = std_arr[k]
    # 오름차순 정렬
    std_arr.sort(reverse = True)
    
    for f in range(0, len(std_arr)):
        if std_arr[f] == ask:
            idx = f
            break
    print(f"#{i+1} {score_arr[idx//(len(std_arr)//10)]}")