

def recur(N):
    if N == 0: return 1
    return N * recur(N-1)

N = int(input())
print(recur(N))