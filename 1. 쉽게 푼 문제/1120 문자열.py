import sys

a, b = input().split()
result = sys.maxsize

for i in range(len(b) - len(a) + 1):
    dist = 0
    
    for j in range(len(a)):
        if a[j] != b[i + j]:
            dist += 1

    result = min(result, dist)

print(result)
