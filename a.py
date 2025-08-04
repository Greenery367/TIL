# 테스트 케이스의 수
T = int().input()
# n : 총 학생 수
# k : 학점을 알고 싶은 학생의 번호
n, k = map(int, input().split())
# 점수 리스트
score_arr = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 
             'C+', 'C0', 'C-', 'D0']
# 모든 학생들의 점수 리스트
std_arr = []
for i in n :
    mid, fin, hom = map(int, input().split())
    std_arr.append(mid*0.35 + fin*0.45 + hom*0.2)
    