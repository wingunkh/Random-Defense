import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        now_r, now_c, now_k = q.popleft()

        if now_r == n - 1 and now_c == m - 1:
            return visited[now_r][now_c][now_k] - 1

        for i in range(4):
            next_r, next_c = now_r + move[i][0], now_c + move[i][1]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if not visited[next_r][next_c][now_k] and a[next_r][next_c] == 0:
                q.append((next_r, next_c, now_k))
                visited[next_r][next_c][now_k] = visited[now_r][now_c][now_k] + 1

        if now_k >= k:
            continue

        for i in range(8):
            next_r, next_c = now_r + jump[i][0], now_c + jump[i][1]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue
            
            if not visited[next_r][next_c][now_k + 1] and a[next_r][next_c] == 0:
                q.append((next_r, next_c, now_k + 1))
                visited[next_r][next_c][now_k + 1] = visited[now_r][now_c][now_k] + 1

    return -1

k = int(input())
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
jump = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

print(bfs())
