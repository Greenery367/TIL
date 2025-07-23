import sys

while True :
    line = sys.stdin.readline()
    
    if not line :
        break
    
    parts = line.strip().split()
    if len(parts) != 2:
        continue
    
    a, b = map(int, parts)
    print(a + b)