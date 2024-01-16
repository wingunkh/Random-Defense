import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()

    for d in range(h):
        for r in range(m):
            for c in range(n):
                if a[d][r][c] == 1:
                    q.append((d, r, c))

    while q:
        now_d, now_r, now_c = q.popleft()

        for i in range(6):
            next_d, next_r, next_c = now_d + dd[i], now_r + dr[i], now_c + dc[i]

            if 0 <= next_d < h and 0 <= next_r < m and 0 <= next_c < n:
                if a[next_d][next_r][next_c] == 0:
                    a[next_d][next_r][next_c] = a[now_d][now_r][now_c] + 1
                    q.append((next_d, next_r, next_c))

n, m, h = map(int, input().split())
a = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dd = [0, 0, 0, 0, -1, 1]
result = 0

bfs()

for d in range(h):
    for r in range(m):
        for c in range(n):
            if a[d][r][c] == 0:
                print(-1)
                exit()
            else:
                result = max(result, a[d][r][c])
else:
    print(result-1)
