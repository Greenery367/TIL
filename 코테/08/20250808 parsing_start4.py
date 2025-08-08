text = 'ABCDEFABCKKKKKABC'
num_of_abc = 0

for i in range(len(text)-2):
    var = text[i:i+3]
    if var == "ABC":
        num_of_abc += 1
print(num_of_abc)