from collections import deque

def dfs(depth):
    global result
    
    if depth == 3:
        result = max(result, bfs())

        return
    
    for r in range(n):
        for c in range(m):
            if a[r][c] == 0:
                a[r][c] = 1
                dfs(depth + 1)
                a[r][c] = 0
    
def bfs():
    q = deque()
    safe = 0

    for r in range(n):
        for c in range(m):
            if a[r][c] == 2:
                q.append((r, c))

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] == 0:
                a[next_r][next_c] = -1
                q.append((next_r, next_c))

    for r in range(n):
        for c in range(m):
            if a[r][c] == 0:
                safe += 1
            elif a[r][c] == -1:
                a[r][c] = 0

    return safe

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

dfs(0)

print(result)
