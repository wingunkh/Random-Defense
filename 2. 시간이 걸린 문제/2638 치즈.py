from collections import deque

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    
    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] == 0 and not visited[next_r][next_c]:
                q.append((next_r, next_c))
                visited[next_r][next_c] = 1
            elif a[next_r][next_c] == 1:
                visited[next_r][next_c] += 1

    for r in range(n):
        for c in range(m):
            if visited[r][c] >= 2:
                a[r][c] = 0

def check():
    for r in range(n):
        for c in range(m):
            if a[r][c] == 1:
                return True

    return False

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

while check():
    result += 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    bfs()

print(result)
