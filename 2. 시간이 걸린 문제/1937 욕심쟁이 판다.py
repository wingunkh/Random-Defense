import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, c):
    if dp[r][c]:
        return dp[r][c]

    dp[r][c] = 1
    
    for i in range(4):
        next_r, next_c = r + dr[i], c + dc[i]

        if not (0 <= next_r < n and 0 <= next_c < n):
            continue

        if a[next_r][next_c] > a[r][c]:
            dp[r][c] = max(dp[r][c], 1 + dfs(next_r, next_c))

    return dp[r][c]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
# dp[r][c] = r행 c열 칸에서 시작했을 때 이동할 수 있는 가장 긴 경로의 길이
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

for r in range(n):
    for c in range(n):
        result = max(result, dfs(r, c))

print(result)
