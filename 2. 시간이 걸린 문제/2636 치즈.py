from collections import deque

def bfs():
    q = deque()
    melt = []
    
    q.append((0, 0))
    visited[0][0] = True

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] == 0 and not visited[next_r][next_c]:
                q.append((next_r, next_c))
                visited[next_r][next_c] = True
            elif a[next_r][next_c] == 1 and not visited[next_r][next_c]:
                melt.append((next_r, next_c))
                visited[next_r][next_c] = True

    for r, c in melt:
        a[r][c] = 0

    return len(melt)

def count_cheese():
    count = 0

    for r in range(n):
        for c in range(m):
            if a[r][c] == 1:
                count += 1

    return count

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
time = 0
cheese_count = count_cheese()

while True:
    time += 1
    visited = [[False for _ in range(m)] for _ in range(n)]

    melt_count = bfs()
    cheese_count -= melt_count

    if cheese_count == 0:
        print(time)
        print(melt_count)
        break
