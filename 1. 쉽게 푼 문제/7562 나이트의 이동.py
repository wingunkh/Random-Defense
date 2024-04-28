import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        now_r, now_c, depth = q.popleft()

        if now_r == end_r and now_c == end_c:
            return depth

        for i in range(8):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if not visited[next_r][next_c]:
                q.append((next_r, next_c, depth + 1))
                visited[next_r][next_c] = True
        
t = int(input())
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(t):
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())

    print(bfs(start_r, start_c))
