import sys, copy
input = sys.stdin.readline

def dust():
    tmp = [[0 for _ in range(m)] for _ in range(n)]
    
    for r in range(n):
        for c in range(m):
            count = 0
            
            if a[r][c] > 0:
                for i in range(4):
                    next_r, next_c = r + dr[i], c + dc[i]

                    if not (0 <= next_r < n and 0 <= next_c < m):
                        continue

                    if a[next_r][next_c] == -1:
                        continue

                    tmp[next_r][next_c] += a[r][c] // 5
                    count += 1

                tmp[r][c] += a[r][c] - a[r][c] // 5 * count
            elif a[r][c] == -1:
                tmp[r][c] = -1

    return tmp

def circulate(boundary, dr, dc):
    r, c = boundary, 1
    previous = 0
    i = 0

    while True:
        next_r, next_c = r + dr[i], c + dc[i]

        if not (0 <= next_r < n and 0 <= next_c < m):
            i = (i + 1) % 4
            continue

        if a[r][c] == -1:
            break

        a[r][c], previous = previous, a[r][c]

        r, c = next_r, next_c

n, m, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
up_r = [0, -1, 0, 1] # 우, 상, 좌, 하
up_c = [1, 0, -1, 0] # 우, 상, 좌, 하
down_r = [0, 1, 0, -1] # 우, 하, 좌, 상
down_c = [1, 0, -1, 0] # 우, 하, 좌, 상
boundary = []
result = 0

for r in range(n):
    for c in range(m):
        if a[r][c] == -1:
            boundary.append(r)

for _ in range(t):
    a = copy.deepcopy(dust())
    circulate(boundary[0], up_r, up_c)
    circulate(boundary[1], down_r, down_c)

for r in range(n):
    for c in range(m):
        if a[r][c] > 0:
            result += a[r][c]

print(result)
