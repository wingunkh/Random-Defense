n = int(input())
a = [[0 for _ in range(101)] for _ in range(101)]
result = 0

for _ in range(n):
    y, x = map(int, input().split())

    for r in range(y, y + 10):
        for c in range(x, x + 10):
            a[r][c] = 1

for r in range(101):
    for c in range(101):
        if a[r][c]:
            result += 1

print(result)
