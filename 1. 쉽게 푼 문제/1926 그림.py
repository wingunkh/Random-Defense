import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    area = 0
    
    q.append((r, c))
    visited[r][c] = True

    while q:
        now_r, now_c = q.popleft()
        area += 1

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] == 1 and not visited[next_r][next_c]:
                q.append((next_r, next_c))
                visited[next_r][next_c] = True

    return area

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result_count = 0
result_area = 0

for r in range(n):
    for c in range(m):
        if a[r][c] == 1 and not visited[r][c]:
            result_count += 1
            result_area = max(result_area, bfs(r, c))

print(result_count)
print(result_area)
