from collections import deque

def bfs(r, c):
    q = deque()
    
    q.append((r, c))
    visited[r][c] = 1

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] == 'L' and not visited[next_r][next_c]:
                q.append((next_r, next_c))
                visited[next_r][next_c] = visited[now_r][now_c] + 1

    return visited[now_r][now_c] - 1

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
edge = []
result = 0

for r in range(n):
    for c in range(m):
        if a[r][c] == 'L':
            visited = [[False for _ in range(m)] for _ in range(n)]
            result = max(result, bfs(r, c))

print(result)

# 트리는 사이클이 없는 무방향 그래프이며, 두 정점을 잇는 경로가 유일함
# 해당 문제는 육지가 트리라는 보장이 없으므로, 트리의 지름 공식 사용 불가
