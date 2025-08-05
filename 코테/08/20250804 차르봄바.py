# T : 테스트 케이스 개수
T = int(input())

# 테스트 케이스 개수만큼 반복
for i in range(T):
    # N : 마을의 크기
    # P : 차르봄바의 파워
    N, P = map(int, input().split())
    town = []
    
    #마을의 크기 N만큼 바이러스 개수 받기
    for j in range(N):
       town.append(list(map(int, input().split()))) 