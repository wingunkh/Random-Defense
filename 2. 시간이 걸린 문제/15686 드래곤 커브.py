n = int(input())
a = [[0 for _ in range(101)] for _ in range(101)]
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
result = 0

for _ in range(n):
    c, r, d, g = map(int, input().split())
    a[r][c] = 1
    direction = [d]

    for _ in range(g):
        for i in range(len(direction) - 1, -1, -1):
            direction.append((direction[i] + 1) % 4)

    for i in direction:
        r, c = r + dr[i], c + dc[i]

        if not (0 <= r < 101 and 0 <= c < 101):
            continue

        a[r][c] = 1

for r in range(100):
    for c in range(100):
        if a[r][c] == 1 and a[r + 1][c] == 1 and a[r][c + 1] == 1 and a[r + 1][c + 1] == 1:
            result += 1

print(result)
