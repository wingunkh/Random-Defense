import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
visited_f = [[False for _ in range(m)] for _ in range(n)]
visited_h = [[False for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
tmp = []

def fire(tmp):
    q = deque()

    for r, c in tmp: 
        q.append((r, c))
        visited_f[r][c] = 1

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] != '#' and not visited_f[next_r][next_c]:
                q.append((next_r, next_c))
                visited_f[next_r][next_c] = visited_f[now_r][now_c] + 1

def human(r, c):
    q = deque()
    q.append((r, c))
    visited_h[r][c] = 1

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                return visited_h[now_r][now_c]

            if a[next_r][next_c] != '#' and not visited_h[next_r][next_c]:
                if not visited_f[next_r][next_c] or visited_f[next_r][next_c] > visited_h[now_r][now_c] + 1:
                    q.append((next_r, next_c))
                    visited_h[next_r][next_c] = visited_h[now_r][now_c] + 1

    return "IMPOSSIBLE"

for r in range(n):
    for c in range(m):
        if a[r][c] == 'F':
            tmp.append((r, c))

fire(tmp)

for r in range(n):
    for c in range(m):
        if a[r][c] == 'J':
            print(human(r, c))
