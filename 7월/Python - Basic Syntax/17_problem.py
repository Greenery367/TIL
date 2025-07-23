total_price = int(input())
num = int(input())

imagine_price = 0

for i in range(num) :
    a, b = map(int, input().split())
    imagine_price += a * b

if total_price == imagine_price :
    print("Yes")
else :
    print("No")