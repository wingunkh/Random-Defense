from collections import deque

def bfs(r, c):
    q = deque()
    q.append((r, c))

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if 0 <= next_r < n and 0 <= next_c < m and a[next_r][next_c] == 1:
                q.append((next_r, next_c))
                a[next_r][next_c] = a[now_r][now_c] + 1

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

bfs(0, 0)

print(a[n-1][m-1])
