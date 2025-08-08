text = [
    ["GOLDABCGOLD"],
    ["HELLOWORLD"],
    ["WHITEGOLD"]
]

def find_gold(arr):
    total_golds = 0

    for i in range(len(arr)):
        for j in range(0, len(arr[i][0])-3, 3):

            num_of_gold = arr[i][0].find('GOLD', j)

            print(f"{i}{j} : {arr[i][0].find('GOLD',j)}")

            if num_of_gold != -1  and arr[i][0].find('GOLD',j) != arr[i][0].find('GOLD',j-3): total_golds += 1

    print(total_golds)


find_gold(text)