from collections import deque

def bfs(r, c):
    q = deque()
    buff = []
    sum = a[r][c]

    q.append((r, c))
    visited[r][c] = True
    buff.append((r, c))
    
    while q:
        now_r, now_c = q.popleft()
        
        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if not visited[next_r][next_c] and s <= abs(a[now_r][now_c] - a[next_r][next_c]) <= e:
                q.append((next_r, next_c))
                visited[next_r][next_c] = True
                buff.append((next_r, next_c))
                sum += a[next_r][next_c]

    if len(buff) > 1:
        for r, c in buff:
            a[r][c] = int(sum / len(buff))

        return True
    else:
        return False

n, s, e = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    moved = False

    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                if bfs(r, c):
                    moved = True

    if moved:
        result += 1
    else:
        print(result)
        break
