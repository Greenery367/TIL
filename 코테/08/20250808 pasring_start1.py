text = "helloworld[92084]answer"
a = 0
b = 0
for i in range(len(text)):
   if text[i] == "[":
       a = i
   if text[i] == "]":
       b = i

for i in range(a+1, b):
    print(*text[i], end="", sep="")