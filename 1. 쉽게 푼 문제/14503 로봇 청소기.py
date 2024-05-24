n, m = map(int, input().split())
r, c, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
result = 0

while True:
    if a[r][c] == 0:
        a[r][c] = 2
        result += 1

    for i in range(4):
        d = (d + 3) % 4
        next_r, next_c = r + dr[d], c + dc[d]

        if not (0 <= next_r < n and 0 <= next_c < m):
            continue

        if a[next_r][next_c] == 0:
            r, c = next_r, next_c
            break
    else:
        next_r, next_c = r + dr[(d + 2) % 4], c + dc[(d + 2) % 4]

        if not (0 <= next_r < n and 0 <= next_c < m):
            break

        if a[next_r][next_c] == 1:
            break

        r, c = next_r, next_c

print(result)
