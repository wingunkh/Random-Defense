import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    
    for r in range(m):
        for c in range(n):
            if a[r][c] == 1:
                q.append((r, c))
                
    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if 0 <= next_r < m and 0 <= next_c < n and a[next_r][next_c] == 0:
                a[next_r][next_c] = a[now_r][now_c] + 1
                q.append((next_r, next_c))

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

bfs()

for r in range(m):
    for c in range(n):
        if a[r][c] > 0:
            result = max(result, a[r][c])
        elif a[r][c] == 0:
            print(-1)
            exit()
else:
    print(result-1)
