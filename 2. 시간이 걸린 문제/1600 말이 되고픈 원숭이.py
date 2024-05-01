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
            next_r, next_c = now_r + dr1[i], now_c + dc1[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if not a[next_r][next_c] and not visited[next_r][next_c][now_k]:
                q.append((next_r, next_c, now_k))
                visited[next_r][next_c][now_k] = visited[now_r][now_c][now_k] + 1

        if now_k < k:
            for i in range(8):
                next_r, next_c = now_r + dr2[i], now_c + dc2[i]

                if not (0 <= next_r < n and 0 <= next_c < m):
                    continue

                if not a[next_r][next_c] and not visited[next_r][next_c][now_k + 1]:
                    q.append((next_r, next_c, now_k + 1))
                    visited[next_r][next_c][now_k + 1] = visited[now_r][now_c][now_k] + 1

    return -1

k = int(input())
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
# visited[행][열][이동 수]
dr1 = [-1, 1, 0, 0]
dc1 = [0, 0, -1, 1]
dr2 = [-1, -2, -2, -1, 1, 2, 2, 1]
dc2 = [-2, -1, 1, 2, 2, 1, -1, -2]

print(bfs())
