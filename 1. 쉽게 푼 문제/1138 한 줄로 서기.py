n = int(input())
a = list(map(int, input().split()))
result = [0 for _ in range(n)]

for height in range(1, n + 1):
    count = a[height - 1]
    
    for i in range(n):
        if result[i] == 0 and count == 0:
            result[i] = height
            break
        elif result[i] == 0:
            count -= 1

print(*result, sep = ' ')
