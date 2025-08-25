T = int(input())
dict = {}
for tc in range(T):
    name, status = input().split()
    dict[name] = status

result = []

for key,value in dict.items():
    if value == 'enter':
        result.append(key)

result.sort(reverse=True)
for i in result : print(i)