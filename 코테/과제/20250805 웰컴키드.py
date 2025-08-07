N = int(input())
part_arr = list(map(int, input().split()))
T, P = map(int, input().split())

total_t_num = 0
total_p_num = 0
total_p_left = 0

for i in part_arr :
    if i % T != 0 :
        total_t_num += i//T + 1
    else :
        total_t_num += i//T
        
total_p_num = N // P
total_p_left = N % P

print(total_t_num)
print(total_p_num, total_p_left)