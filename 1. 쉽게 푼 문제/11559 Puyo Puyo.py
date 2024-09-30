from collections import deque

def bfs(r, c):
    global flag
    
    color = a[r][c]
    q = deque()
    tmp = []
    
    q.append((r, c))
    tmp.append((r, c))
    visited[r][c] = True

    while q:
        now_r, now_c = q.popleft()
        
        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < 12 and 0 <= next_c < 6):
                continue

            if a[next_r][next_c] == color and not visited[next_r][next_c]:
                q.append((next_r, next_c))
                tmp.append((next_r, next_c))
                visited[next_r][next_c] = True

    if len(tmp) >= 4:
        flag = True
        
        for r, c in tmp:
            a[r][c] = '.'

a = [list(input()) for _ in range(12)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

while True:
    visited = [[False for _ in range(6)] for _ in range(12)]
    flag = False

    for r in range(12):
        for c in range(6):
            if a[r][c] != '.' and not visited[r][c]:
                bfs(r, c)

    if not flag:
        break

    result += 1

    for c in range(6):
        for r in range(10, -1, -1):
            if a[r][c] != '.':
                now = r

                while now <= 10 and a[now + 1][c] == '.':
                    a[now + 1][c] = a[now][c]
                    a[now][c] = '.'
                    now += 1

print(result)
