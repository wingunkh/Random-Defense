import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r, c))
    a[r][c] = 0

    while q:
        now_r, now_c = q.popleft()

        for i in range(8):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < h and 0 <= next_c < w):
                continue

            if a[next_r][next_c] == 1:
                q.append((next_r, next_c))
                a[next_r][next_c] = 0

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    
    a = [list(map(int, input().split())) for _ in range(h)]
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    result = 0

    for r in range(h):
        for c in range(w):
            if a[r][c] == 1:
                bfs(r, c)
                result += 1

    print(result)
