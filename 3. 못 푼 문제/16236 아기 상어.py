from collections import deque

def bfs(r, c, size):
    q = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    distance = [[0 for _ in range(n)] for _ in range(n)]
    fish = []

    q.append((r, c))
    visited[r][c] = True

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if not visited[next_r][next_c] and size >= a[next_r][next_c]:
                q.append((next_r, next_c))
                visited[next_r][next_c] = True
                distance[next_r][next_c] = distance[now_r][now_c] + 1

                if 0 < a[next_r][next_c] < size:
                    fish.append((next_r, next_c, distance[next_r][next_c]))

    return sorted(fish, key = lambda x: (x[2], x[0], x[1]))

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
shark_r, shark_c = 0, 0
size = 2
count = 0
result = 0

for r in range(n):
    for c in range(n):
        if a[r][c] == 9:
            shark_r, shark_c = r, c
            a[shark_r][shark_c] = 0

while True:
    fish = bfs(shark_r, shark_c, size)

    if len(fish) == 0:
        print(result)
        break

    shark_r, shark_c, time = fish[0]
    result += time
    count += 1
    a[shark_r][shark_c] = 0

    if count == size:
        size += 1
        count = 0
