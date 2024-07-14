import sys
from collections import deque
input = sys.stdin.readline

def bfs1(r, c, count):
    q = deque()
    q.append((r, c))
    visited[r][c] = True

    while q:
        now_r, now_c = q.popleft()
        a[now_r][now_c] = count

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if a[next_r][next_c] == 1 and not visited[next_r][next_c]:
                q.append((next_r, next_c))
                visited[next_r][next_c] = True

def bfs2(number):
    q = deque()

    for r in range(n):
        for c in range(n):
            if a[r][c] == number:
                q.append((r, c, 0))
                visited[r][c] = True
                
    while q:
        now_r, now_c, depth = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if a[next_r][next_c] != 0 and a[next_r][next_c] != number:
                return depth

            if a[next_r][next_c] == 0 and not visited[next_r][next_c]:
                q.append((next_r, next_c, depth + 1))
                visited[next_r][next_c] = True

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
count = 0
result = sys.maxsize

visited = [[False for _ in range(n)] for _ in range(n)]

for r in range(n):
    for c in range(n):
        if a[r][c] == 1 and not visited[r][c]:
            count += 1
            bfs1(r, c, count)

for number in range(1, count + 1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = min(result, bfs2(number))

print(result)
