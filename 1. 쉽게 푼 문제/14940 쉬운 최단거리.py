import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        now_r, now_c, depth = q.popleft()

        if a[now_r][now_c] == 1:
            result[now_r][now_c] = depth

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] > 0 and not visited[next_r][next_c]:
                q.append((next_r, next_c, depth + 1))
                visited[next_r][next_c] = True

    return -1
        
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = [[0 for _ in range(m)] for _ in range(n)]

for r in range(n):
    for c in range(m):
        if a[r][c] == 2:
            bfs(r, c)

for r in range(n):
    for c in range(m):
        if a[r][c] == 1 and not visited[r][c]:
            print(-1, end = ' ')
        else:
            print(result[r][c], end = ' ')
    else:
        print()
