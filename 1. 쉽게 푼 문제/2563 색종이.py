a = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
result = 0

for _ in range(n):
    x, y = map(int, input().split())
    start_r, start_c = y, x
    
    for r in range(start_r, start_r + 10):
        for c in range(start_c, start_c + 10):
            a[r][c] = 1

for r in range(101):
    for c in range(101):
        if a[r][c] == 1:
            result += 1

print(result)
