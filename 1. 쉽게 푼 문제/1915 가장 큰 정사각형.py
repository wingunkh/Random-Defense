import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, list(input().rstrip()))) for _ in range(n)]
result = 0

for r in range(1, n):
    for c in range(1, m):
        if dp[r][c] == 1:
            if dp[r - 1][c - 1] > 0 and dp[r - 1][c] > 0 and dp[r][c - 1] > 0:
                dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1

for r in range(n):
    for c in range(m):
        result = max(result, dp[r][c])

print(result ** 2)
