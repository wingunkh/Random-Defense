import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if 0 <= next_r < n and 0 <= next_c < n:
                if a[next_r][next_c] == a[r][c] and not visited[next_r][next_c]:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = True

n = int(input())
a = [list(input().rstrip()) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result1 = 0
result2 = 0

visited = [[False for _ in range(n)] for _ in range(n)]

for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            bfs(r, c)
            result1 += 1

visited = [[False for _ in range(n)] for _ in range(n)]

for r in range(n):
    for c in range(n):
        if a[r][c] == 'G':
            a[r][c] = 'R'

for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            bfs(r, c)
            result2 += 1
            
print(result1, result2)
