import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, c):
    total = 0

    if r == n - 1 and c == m - 1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    for i in range(4):
        next_r, next_c = r + dr[i], c + dc[i]

        if not (0 <= next_r < n and 0 <= next_c < m):
            continue

        if a[next_r][next_c] < a[r][c]:
            total += dfs(next_r, next_c)

    dp[r][c] = total

    return dp[r][c]

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
# dp[i][j] = i행 j열에서 목적지까지 도달 가능한 모든 경로의 수
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

print(dfs(0, 0))
