import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()

    a[r][c] = 0
    q.append((r, c))

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if 0 <= next_r < n and 0 <= next_c < m and a[next_r][next_c] == 1:
                a[next_r][next_c] = 0
                q.append((next_r, next_c))

t = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(t):
    m, n, k = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    result = 0

    for _ in range(k):
        c, r = map(int, input().split())
        a[r][c] = 1

    for r in range(n):
        for c in range(m):
            if a[r][c] == 1:
                bfs(r, c)
                result += 1

    print(result)
