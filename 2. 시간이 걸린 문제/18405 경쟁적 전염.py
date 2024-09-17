import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque(start)

    while q:
        number, now_r, now_c, depth = q.popleft()

        if depth == s:
            return

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if not visited[next_r][next_c]:
                q.append((number, next_r, next_c, depth + 1))
                visited[next_r][next_c] = number

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
s, x, y = map(int, input().split())
start = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(n):
    for c in range(n):
        if a[r][c] != 0:
            start.append((a[r][c], r, c, 0))
            visited[r][c] = a[r][c]

start.sort(key = lambda x: x[0])
bfs()

print(visited[x - 1][y - 1])
