def bfs(r, c, rain):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if 0 <= next_r < n and 0 <= next_c < n and a[next_r][next_c] > rain:
                if not visited[next_r][next_c]:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = True

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 1

for rain in range(100):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for r in range(n):
        for c in range(n):
            if a[r][c] > rain and not visited[r][c]:
                bfs(r, c, rain)
                count += 1

    result = max(result, count)

print(result)
