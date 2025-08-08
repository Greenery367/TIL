text = 'B[45]AB[9994]'
start_arr = []
end_arr = []
result = 0
start_point = 0

for i in range(len(text)):
    if text.find('[', start_point) != -1 :
        start_arr.append(text.find('[', start_point))
        end_arr.append(text.find(']', start_point))
        start_point = text.find(']', start_point) +1

for j in range(len(start_arr)):
    result += int(text[start_arr[j]+1:end_arr[j]])

print(result)