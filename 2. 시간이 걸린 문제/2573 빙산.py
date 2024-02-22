import sys
from collections import deque
input = sys.stdin.readline

def melt(r, c):
    for i in range(4):
        next_r, next_c = r + dr[i], c + dc[i]

        if not (0 <= next_r < n and 0 <= next_c < m):
            continue

        if a[next_r][next_c] == 0:
            a[r][c] -= 1

        if a[r][c] == 0:
            a[r][c] = -1

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] != 0 and not visited[next_r][next_c]:
                q.append((next_r, next_c))
                visited[next_r][next_c] = True

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0
            
while True:
    result += 1
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0

    for r in range(n):
        for c in range(m):
            if a[r][c] != 0:
                melt(r, c)

    for r in range(n):
        for c in range(m):
            if a[r][c] < 0:
                a[r][c] = 0

    for r in range(n):
        for c in range(m):
            if a[r][c] != 0 and not visited[r][c]:
                count += 1
                bfs(r, c)

    if count > 1:
        print(result)
        break
    elif count == 0:
        print(0)
        break
