a = [[0 for _ in range(101)] for _ in range(101)]
result = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for r in range(y1, y2):
        for c in range(x1, x2):
            a[r][c] = 1

for r in range(101):
    for c in range(101):
        if a[r][c]:
            result += 1

print(result)
