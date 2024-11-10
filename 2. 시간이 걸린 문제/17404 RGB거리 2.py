import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
result = sys.maxsize

for start in range(3):
    dp = [[sys.maxsize for _ in range(3)] for _ in range(n)]
    # dp[i][j] = i번째 집을 j색으로 칠할 때 필요한 누적 비용

    dp[0][start] = a[0][start]

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + a[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + a[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + a[i][2]

    for i in range(3):
        if i == start:
            continue

        result = min(result, dp[n - 1][i])

print(result)
