text = "BBQBHCKFCMC"
a = "KFC"
for i in range(len(text) -3):
    if text[i]+text[i+1]+text[i+2] == a :
        print(i)