T = int(input())

for i in range(1, T+1):
    N,K = map(int, input().split())
    N_arr = list(map(int, input().split()))
    K_arr = list(map(int, input().split()))

    nums = 0  # K_arr를 따라갈 포인터
    for n in N_arr:
        if nums < K and n == K_arr[nums]:
            nums += 1  # 현재 passcode 숫자 찾았으니 다음으로 넘어감

    if nums == K:
        print(f"#{i} {1}")
    else:
        print(f"#{i} {0}")
