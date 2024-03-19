from collections import deque

def bfs():
    q = deque()

    for d in range(h):
        for r in range(n):
            for c in range(m):
                if a[d][r][c] == 1:
                    q.append((d, r, c))

    while q:
        now_d, now_r, now_c = q.popleft()

        for i in range(6):
            next_d, next_r, next_c = now_d + dd[i], now_r + dr[i], now_c + dc[i]

            if not (0 <= next_d < h and 0 <= next_r < n and 0 <= next_c < m):
                continue
            
            if a[next_d][next_r][next_c] == 0:
                q.append((next_d, next_r, next_c))
                a[next_d][next_r][next_c] = a[now_d][now_r][now_c] + 1

m, n, h = map(int, input().split())
a = []
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dd = [0, 0, 0, 0, -1, 1]
result = 0

for _ in range(h):
    buff = []
    
    for _ in range(n):
        buff.append(list(map(int, input().split())))

    a.append(buff)

bfs()

for d in range(h):
    for r in range(n):
        for c in range(m):
            if a[d][r][c] == 0:
                print(-1)
                exit()
            elif a[d][r][c] >= 1:
                result = max(result, a[d][r][c])

print(result - 1)
