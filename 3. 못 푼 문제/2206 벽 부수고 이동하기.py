import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        now_r, now_c, flag = q.popleft()

        if now_r == n-1 and now_c == m-1:
            return visited[now_r][now_c][flag]

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] == 1 and flag == 0:
                q.append((next_r, next_c, 1))
                visited[next_r][next_c][1] = visited[now_r][now_c][0] + 1
            elif a[next_r][next_c] == 0 and not visited[next_r][next_c][flag]:
                q.append((next_r, next_c, flag))
                visited[next_r][next_c][flag] = visited[now_r][now_c][flag] + 1

    return -1
    
n, m = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

print(bfs())
