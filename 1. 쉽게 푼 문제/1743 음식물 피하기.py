import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, c):
    visited[r][c] = True
    size = 1

    for i in range(4):
        next_r, next_c = r + dr[i], c + dc[i]

        if not (0 <= next_r < n and 0 <= next_c < m):
            continue

        if a[next_r][next_c] == 1 and not visited[next_r][next_c]:
            size += dfs(next_r, next_c)

    return size

n, m, k = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

for _ in range(k):
    r, c = map(int, input().split())
    a[r - 1][c - 1] = 1

for r in range(n):
    for c in range(m):
        if a[r][c] == 1 and not visited[r][c]:
            result = max(result, dfs(r, c))

print(result)
