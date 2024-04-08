from collections import deque

def bfs(r, c):
    q = deque()
    buff = []
    sum = a[r][c]
    
    q.append((r, c))
    buff.append((r, c))
    visited[r][c] = True

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if not visited[next_r][next_c] and s <= abs(a[now_r][now_c] - a[next_r][next_c]) <= e:
                q.append((next_r, next_c))
                buff.append((next_r, next_c))
                visited[next_r][next_c] = True
                sum += a[next_r][next_c]

    if len(buff) > 1:
        for i in range(len(buff)):
            r, c = buff[i]
            a[r][c] = int(sum / len(buff))

        return True
    else:
        return False
    
n, s, e = map(int, input().split())
a = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

for _ in range(n):
    a.append(list(map(int, input().split())))

while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    moved = False

    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                if bfs(r, c):
                    moved = True

    if not moved:
        print(result)
        break
    else:
        result += 1
