import sys
from collections import deque
input = sys.stdin.readline

def move_fire(fire):
    q = deque()

    for r, c in fire:
        q.append((r, c))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if not (0 <= nr < n and 0 <= nc < m):
                continue

            if a[nr][nc] == '.':
                q.append((nr, nc))
                a[nr][nc] = a[r][c] + 1

def escape(now):
    q = deque()
    q.append((now))

    while q:
        r, c, depth = q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if not (0 <= nr < n and 0 <= nc < m):
                return depth + 1

            if a[nr][nc] == '#':
                continue

            if a[nr][nc] == '.' and not visited[nr][nc]: # 불이 나지 않는 빌딩 이동 처리
                q.append((nr, nc, depth + 1))
                visited[nr][nc] = True
            elif a[nr][nc] != '.' and depth + 1 < a[nr][nc] and not visited[nr][nc]: # 불이 난 빌딩 이동 처리
                q.append((nr, nc, depth + 1))
                visited[nr][nc] = True

    return "IMPOSSIBLE"
    
t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    a = [list(input().rstrip()) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    now = 0
    fire = []

    for r in range(n):
        for c in range(m):
            if a[r][c] == '@':
                now = (r, c, 0)
                a[r][c] = '.'
            elif a[r][c] == '*':
                fire.append((r, c))
                a[r][c] = 0

    move_fire(fire)
    print(escape(now))
