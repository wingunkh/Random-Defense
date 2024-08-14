import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0, 0))

    while q:            
        now_r, now_c = q.popleft()

        if now_r == n - 1 and now_c == m - 1:
            continue

        for i in range(2):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if dp[now_r][now_c] + a[next_r][next_c] > dp[next_r][next_c]:
                dp[next_r][next_c] = dp[now_r][now_c] + a[next_r][next_c]
                q.append((next_r, next_c))

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
dp[0][0] = a[0][0]
dr = [1, 0]
dc = [0, 1]

bfs()

print(dp[-1][-1])
