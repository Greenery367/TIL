arr = [
    ['ABCQ'],
    ['B[4]R'],
    ['CCDA'],
    ['BT[15]']
]

def get_find(arr):
    for i in range(len(arr)):
        start = arr[i][0].find('[',0)
        end = arr[i][0].find(']',0)

        if start != -1 and end != -1 :
            print(arr[i][0][start+1:end],end= " ")


get_find(arr)