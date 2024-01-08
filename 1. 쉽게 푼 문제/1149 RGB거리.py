n = int(input())
a = [(0, 0, 0)]
dp = [[0 for _ in range(3)] for _ in range(n+1)]
# dp[i][j] = i번 집을 j색으로 칠했을 때 i번 집까지 칠했을 때의 최소 비용

for _ in range(n):
    r, g, b = map(int, input().split())
    a.append((r, g, b))

for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1] + a[i][0], dp[i-1][2] + a[i][0])
    dp[i][1] = min(dp[i-1][0] + a[i][1], dp[i-1][2] + a[i][1])
    dp[i][2] = min(dp[i-1][0] + a[i][2], dp[i-1][1] + a[i][2])

print(min(dp[n]))
