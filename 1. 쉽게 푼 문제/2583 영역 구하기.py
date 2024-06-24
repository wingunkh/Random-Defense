import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    count = 0
    
    q.append((r, c, 1))
    visited[r][c] = True
    count += 1

    while q:
        now_r, now_c, depth = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] == 0 and not visited[next_r][next_c]:
                q.append((next_r, next_c, depth + 1))
                visited[next_r][next_c] = True
                count += 1

    return count

n, m, k = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    # x1, y1 = 좌상단
    # x2, y2 = 우하단
    x2, y2 = x2 - 1, y2 - 1

    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            a[i][j] = 1

for r in range(n):
    for c in range(m):
        if a[r][c] == 0 and not visited[r][c]:
            result.append(bfs(r, c))

result.sort()

print(len(result))
print(*result)
