from collections import deque

def bfs():
    q = deque()
    
    for d in range(k):
        for r in range(n):
            for c in range(m):
                if a[d][r][c] == 1:
                    q.append((d, r, c))

    while q:
        now_d, now_r, now_c = q.popleft()

        for i in range(6):
            next_d, next_r, next_c = now_d + dd[i], now_r + dr[i], now_c + dc[i]

            if not (0 <= next_d < k and 0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_d][next_r][next_c] == 0:
                q.append((next_d, next_r, next_c))
                a[next_d][next_r][next_c] = a[now_d][now_r][now_c] + 1

m, n, k = map(int, input().split())
a = []
dd = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, -1, 1, 0, 0]
dc = [0, 0, 0, 0, -1, 1]
flag = True
result = 0

for _ in range(k):
    tmp = [list(map(int, input().split())) for _ in range(n)]
    a.append(tmp)

bfs()

for d in range(k):
    for r in range(n):
        for c in range(m):
            if a[d][r][c] == 0:
                flag = False
            else:
                result = max(result, a[d][r][c])

if flag:
    print(result - 1)
else:
    print(-1)
