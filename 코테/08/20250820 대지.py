N = int(input())
X = []
Y = []

for n in range(N) :
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
result = (max(X) - min(X)) * (max(Y) - min(Y))
print(result)