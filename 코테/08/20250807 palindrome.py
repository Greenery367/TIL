while True:
    string_a = str(input())

    if string_a == "0" :
        break

    for i in range(1, len(string_a)):
        stop_point = len(string_a) // 2
        if int(string_a) < 10:
            print("no")
            break

        if string_a[i-1] != string_a[len(string_a)-i] :
            print("no")
            break

    print("yes")